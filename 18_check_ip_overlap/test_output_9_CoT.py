import pytest

import ipaddress
from output_9_CoT import check_ip_overlap

class Testcheck_ip_overlap:
    def test_check_ip_overlap_2(self):
        assert check_ip_overlap('192.168.1.0/24', '192.168.1.0/24') == True

    def test_check_ip_overlap_3(self):
        assert check_ip_overlap('10.0.0.0/8', '10.0.0.0/16') == True

    def test_check_ip_overlap_4(self):
        assert check_ip_overlap('172.16.0.0/12', '192.168.0.0/16') == False

    def test_check_ip_overlap_5(self):
        assert check_ip_overlap('172.16.0.0/12', '172.16.0.0/16') == True

    def test_check_ip_overlap_6(self):
        assert check_ip_overlap('10.0.0.0/8', '172.16.0.0/12') == False

    def test_check_ip_overlap_7(self):
        assert check_ip_overlap('0.0.0.0/0', '192.168.1.0/24') == True

    def test_check_ip_overlap_8(self):
        assert check_ip_overlap('0.0.0.0/0', '0.0.0.0/0') == True

    def test_check_ip_overlap_9(self):
        assert check_ip_overlap('255.255.255.255/32', '255.255.255.255/32') == True

    def test_check_ip_overlap_10(self):
        assert check_ip_overlap('255.255.255.255/32', '0.0.0.0/0') == True
