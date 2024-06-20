from ipaddress import ip_network

def check_ip_overlap(range1: str, range2: str) -> bool:
    network1 = ip_network(range1)
    network2 = ip_network(range2)
    return network1.overlaps(network2)
