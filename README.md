# Personal Firewall in Python

This is a simple *Personal Firewall* project built using *Python* and *Scapy*.  
It allows you to *monitor incoming network packets* and *block traffic from specific IP addresses*.

## Features

- Monitors live network traffic
- Displays each packet's summary
- Blocks packets from *specified suspicious or malicious IP addresses*

## Requirements

- Python 3.x  
- Scapy (Install using pip install scapy)

## How to Run

1. Open *Command Prompt*
2. Navigate to your project folder:
   ```bash
   cd path\to\your\project
3. Run the script:
bash
python firewall.py

## How It Works

- The program uses Scapy's sniff() function to capture incoming network packets.
- For every captured packet, it checks the source IP address.
- If the IP address is found in the blocked list, it prints a message indicating that the packet was blocked.
-
Author:(Gayathri Gurualmiki)
