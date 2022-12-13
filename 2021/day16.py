
data = """\
D2FE28
"""


import pytest
from pathlib import Path

input_filename = Path(__file__).stem + ".input"
print("Reading from: " + input_filename)
#data = Path(input_filename).read_text()


as_bits = "".join(format(int(c, base=16), 'b') for c in data.strip())

print(as_bits)

def decode_packet(data):
    version, data = parse_version(data)
    print(f"Version: {version}")
    type_id, data = parse_version(data)
    print(f"Version: {type_id}")
    packet = dict(version=version, type_id=type_id) 
    if type_id == 4:
        literal, data = parse_literal(data)
        packet['literal'] = literal
    else:
        packets, data = parse_operator(data)
        packet['packets'] = packets

    return packet, data

# 3 bits -> version
# 3 bits -> type ID
#
# type ID 4 -> literal value


def parse_version(data):
    version = int(data[:3], base=2)
    remaining = data[3:]
    return version, remaining

def parse_literal(data):
    num_bits = ""
    while True:
        start = data[:1]
        num_bits += data[1:5]
        data = data[5:]
        if start == "0":
            break
    while data[0] == "0":
        data = data[1:]
    return int(num_bits, base=2), data

def parse_operator(data):
    version, data = parse_version(data)
    type_id, data = parse_version(data)
    length_type_id, data = data[0], data[1:]
    packets = []
    if length_type_id == "0":
        length_of_packets, data = int(data[:15], base=2), data[15:]
        print(f"Need to read {length_of_packets} worth of packets. Can't!")
        exit()
    elif length_type_id == "1":
        num_packets, data = int(data[:11], base=2), data[11:]
        for _ in range(num_packets):
            packet, data = decode_packet(data)
            packets.append(packet)

    return [], dict(version=version, type_id=type_id)

decode_packet(as_bits)

@pytest.parameterize()
def test_decode():

