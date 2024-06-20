import ipaddress

def check_ip_overlap(range1, range2):
    net1 = ipaddress.ip_network(range1)
    net2 = ipaddress.ip_network(range2)
    
    return net1.overlaps(net2)
