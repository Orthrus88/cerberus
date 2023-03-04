from scapy.all import *
from scapy.layers.tls.record_tls13 import TLS13

def handle_packet(packet):
    """
    Processes a captured packet and checks if it contains the string "password".
    """
    # Check if the packet contains a TCP layer
    if TLS13 in packet:
        # Check if the payload contains the string "password"
        if b"password" in packet[TLS13].payload:
            print("Password detected!")
    
# Define a capture filter for all TCP traffic
capture_filter = 'tcp'

# Start capturing traffic on the default interface
capture = sniff(filter=capture_filter, prn=lambda x: handle_packet(x))