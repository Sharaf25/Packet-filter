import socket
import struct
import textwrap

#unpack ethernet frame and return the result
def En_frame(data):
    dest_mac,src_mac,protocol = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac),get_mac_addr(src_mac), socket.htons(protocol), data[14:]

#return formatted MAC address   (AA:BB:CC:DD:EE:FF)
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

def main():
    connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, addr = connection.recvfrom(65536)
        dest_mac, src_mac, eth_proto, data = En_frame(raw_data)
        print('\nEthernet Frame: ')
        print('Destination: {}, Source{}, Protocol: {}'.format(dest_mac,src_mac,eth_proto))

main()