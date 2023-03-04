from scapy.all import *
from scapy.layers.tls.record_tls13 import TLS13

# Process each captured packet
def handle_packet(packet):
    """
    Processes a captured packet and prints details about the TLS handshake if present.
    """
    print(f"Captured packet: {packet.summary()}")

    if TLS13 in packet:
        print("TLS handshake detected!")
        
        # Extract details about the TLS handshake
        version = packet[TLS13].version
        cipher_suite = packet[TLS13].cipher_suite
        handshake_type = packet[TLS13].msg[0].msgtype
        
        # Print the TLS handshake details
        print(f"TLS Version: {version}\nCipher Suite: {cipher_suite}\nHandshake Type: {handshake_type}\n")
    else:
        print("No TLS handshake found in packet.")

# Define a capture filter for HTTPS traffic
capture_filter = 'tcp port 443'

# Start capturing traffic on the default interface
capture = sniff(filter=capture_filter, prn=lambda x: handle_packet(x))
