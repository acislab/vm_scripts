#!/usr/bin/python3
#
# Output CSV that contains a line for each machine to be set up with all the
# information needed by various tools

import ipaddress

# hostname configuration
hostname_prefix = "ece-acis-dc"
hostname_first_part = range(1, 20+1)
hostname_second_part = range(1, 3+1)
domainname = "acis.ufl.edu"

# IP address configuration
start_ip = "10.244.39.100"

# mac address configuration
mac_prefix = "00:50:56:1F"

loop_count = 0
# header isn't needed for out workflow
#print("fqdn,hostname,ip,mac")

for first in hostname_first_part:
    for second in hostname_second_part:
        
        hostname = "{0}{1:02d}{2:02d}".format(hostname_prefix, first, second)
        if len(hostname) > 15:
            print ("WARNING hostname {0} is not AD compliant".format(hostname))


        ip_address = ipaddress.IPv4Address(start_ip) + loop_count
        
        octets = ip_address.exploded.split(".")
        mac_address = "{0}:{1:02x}:{2:02x}".format(mac_prefix,
            int(octets[2]), int(octets[3]))

        print(",".join([".".join([hostname, domainname]), hostname,
            ip_address.exploded, mac_address]))

        loop_count += 1
