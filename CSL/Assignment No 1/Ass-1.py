from scapy.all import *

def packet_handler(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        length = len(packet)
        print(f"IP Packet: Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}, Length: {length}")

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"  TCP Packet: Source Port: {src_port}, Destination Port: {dst_port}")

        if UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"  UDP Packet: Source Port: {src_port}, Destination Port: {dst_port}")

# Start sniffing packets
print("Sniffing packets... Press Ctrl+C to stop.")
sniff(prn=packet_handler, store=0)
