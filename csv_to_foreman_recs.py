#!/usr/bin/python3
#
# Create records in Foreman from CSV
#
# Foreman pkg docs: http://python-foreman.readthedocs.io/en/latest/basic/
# Foreman api docs: https://theforeman.org/api/1.14/index.html

import sys
import fileinput
from foreman.client import Foreman

with open("password_foreman.txt") as f:
    password_foreman = f.readline().rstrip()

fore = Foreman(url="https://foreman-crn.acis.ufl.edu", api_version=2,
    auth=('mjcollin', password_foreman))

for line in fileinput.input():
    fields = line.split(",")
    fqdn = fields[0]
    hostname = fields[1]
    ip = fields[2]
    mac = fields[3]

    fore.hosts.create(
        host={
            "name": fqdn,
            "ip":   ip,
            "mac":  mac,
            "build": True,
            "hostgroup_id": "32"   # tried using *_name but didn't work, had to go 
                                    # get id from database:
                                    # select id,name,title from hostgroups;
            }
    )

