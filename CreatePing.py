"""
Exercise 7.5 - Ping
Author: Noam Cohen
Purpose: write a simple plan that send Echo request and get the reply.
Note: The code is written in a simple way, with remarks and explains how the plan working
"""


# Import modules:
from scapy.all import *
from scapy.layers.inet import IP, ICMP


# Set constants:
ADDRESS = "www.facebook.com"
TYPE = "echo-request"
PROTOCOL = "icmp"


def main():
    request_packet1 = IP(dst=ADDRESS, proto=PROTOCOL) / ICMP(type=TYPE, id=1) / "Noam Cohen 213330616"
    request_packet2 = IP(dst=ADDRESS, proto=PROTOCOL) / ICMP(type=TYPE, id=2) / "Noam Cohen 213330616"
    response_packet1 = sr1(request_packet1)
    response_packet2 = sr1(request_packet2)
    response_packet1.show()
    response_packet2.show()


if __name__ == "__main__":
    main()
