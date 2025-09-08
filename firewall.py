# 🛡️ Simple Personal Firewall in Python

from scapy.all import sniff  # Importing our packet detective tool

# 🎯 This function runs every time a packet (visitor) comes to your system
def packet_callback(packet):
    print("🚨 A packet was found:")
    print(packet.summary())  # Show a short summary of the packet

# 🧪 Let's sniff 10 packets for now to test
print("🔍 Watching your network... Let’s see who comes and goes...")
sniff(prn=packet_callback, count=10)  # count=10 means watch 10 packets then stop
