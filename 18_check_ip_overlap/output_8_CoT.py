import ipaddress

def check_ip_overlap(ip_range1, ip_range2):
    # Parse the IP ranges using the ipaddress module
    network1 = ipaddress.ip_network(ip_range1)
    network2 = ipaddress.ip_network(ip_range2)
    
    # Check if the two networks overlap
    return network1.overlaps(network2)
