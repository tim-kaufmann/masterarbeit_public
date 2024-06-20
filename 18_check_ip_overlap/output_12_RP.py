from ipaddress import ip_network

def check_ip_overlap(range1, range2):
    net1 = ip_network(range1)
    net2 = ip_network(range2)
    return net1.overlaps(net2)
