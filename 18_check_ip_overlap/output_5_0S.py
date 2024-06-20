from ipaddress import ip_network

def check_ip_overlap(range1: str, range2: str) -> bool:
    net1 = ip_network(range1)
    net2 = ip_network(range2)
    return net1.overlaps(net2)
