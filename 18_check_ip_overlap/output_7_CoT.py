from ipaddress import ip_network

def check_ip_overlap(range1: str, range2: str) -> bool:
    # Convert the IP ranges to network objects
    network1 = ip_network(range1)
    network2 = ip_network(range2)
    
    # Check for overlap
    return network1.overlaps(network2)
