from pathlib import Path
from functools import reduce
from operator import mul


def to_int(binary):
    return int(binary, 2)


def parse_packet_opening(packet):
    return to_int(packet[:3]), to_int(packet[3:6]), packet[6:]


def part_one(packet, res=0):
    p_version, p_type, packet = parse_packet_opening(packet)
    res += p_version
    if p_type == 4:
        for i in range(0, len(packet), 5):
            if packet[i] == '0':
                packet = packet[i+5:]
                break
    else:
        if packet[0] == '0':
            packet = packet[16:]
        else:
            packet = packet[12:]
    if '1' in packet:
        return part_one(packet, res)
    return res


def parse_packet(packet):
    p_version, p_type, packet = parse_packet_opening(packet)
    if p_type == 4:
        res = ''
        for i in range(0, len(packet), 5):
            res += packet[i+1:i+5]
            if packet[i] == '0':
                return packet[i+5:], to_int(res)
    length_type_id, packet = packet[0], packet[1:]
    subpackets = []
    if length_type_id == '0':
        bit_count, packet = to_int(packet[:15]), packet[15:]
        subpacket_str = packet[:bit_count]
        packet = packet[bit_count:]
        while subpacket_str:
            subpacket_str, value = parse_packet(subpacket_str)
            subpackets.append(value)
    else:
        subpacket_count, packet = to_int(packet[:11]), packet[11:]
        for _ in range(subpacket_count):
            packet, value = parse_packet(packet)
            subpackets.append(value)
    return packet, operators[p_type](subpackets)


if __name__ == '__main__':
    puzzle_input = Path('input.txt').read_text()
    puzzle_input = bin(int(puzzle_input, 16))[2:].zfill(len(puzzle_input)*4)
    operators = {
        0: lambda x: sum(x),
        1: lambda x: reduce(mul, x),
        2: lambda x: min(x),
        3: lambda x: max(x),
        5: lambda x: 1 if x[0] > x[1] else 0,
        6: lambda x: 1 if x[0] < x[1] else 0,
        7: lambda x: 1 if len(set(x)) == 1 else 0,
    }
    print(f'Part one: {part_one(puzzle_input)}')
    print(f'Part two: {parse_packet(puzzle_input)[1]}')
