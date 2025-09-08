from scapy.all import sniff

# 🚫 List of bad guys we want to block
blocked_ips = ["192.168.1.100", "10.0.0.5"]

def packet_callback(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        if src_ip in blocked_ips:
            print(f"🚫 Blocked packet from {src_ip}")
        else:
            print(f"✅ Safe packet from {src_ip}")
    else:
        print("🔍 Not an IP packet")

print("🚦 Monitoring traffic...")
sniff(prn=packet_callback, count=10)