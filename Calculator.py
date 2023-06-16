def calculate_network_broadcast(ip1, ip2):
    network_address = ip1 & ip2
    broadcast_address = ip1 | (ip2 ^ 0xFFFFFFFF)
    return network_address, broadcast_address

ip1_str = input("Enter IP address:  ")
ip2_str = input("Enter Subnet mask:  ")

ip1 = sum(int(x) << (24 - i*8) for i, x in enumerate(ip1_str.split('.')))
ip2 = sum(int(x) << (24 - i*8) for i, x in enumerate(ip2_str.split('.')))

network, broadcast = calculate_network_broadcast(ip1, ip2)

network_address = '.'.join(str((network >> i) & 255) for i in (24, 16, 8, 0))
broadcast_address = '.'.join(str((broadcast >> i) & 255) for i in (24, 16, 8, 0))

print("Network Address:", network_address)
print("Broadcast Address:", broadcast_address)