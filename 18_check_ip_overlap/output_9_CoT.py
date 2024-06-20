import ipaddress

def check_ip_overlap(range1, range2):
    network1 = ipaddress.ip_network(range1)
    network2 = ipaddress.ip_network(range2)
    
    return network1.overlaps(network2)
