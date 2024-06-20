import ipaddress

def check_ip_overlap(range1: str, range2: str) -> bool:
    net1 = ipaddress.ip_network(range1)
    net2 = ipaddress.ip_network(range2)
    return net1.overlaps(net2)
