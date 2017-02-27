#!/usr/bin/python3
#
# Create records in Foreman from CSV
#
# Foreman pkg docs: http://python-foreman.readthedocs.io/en/latest/basic/
# Foreman api docs: https://theforeman.org/api/1.14/index.html

import fileinput
from foreman.client import Foreman

with open("password_foreman.txt") as f:
    password_foreman = f.readline().rstrip()

fore = Foreman(url="https://foreman-crn.acis.ufl.edu", api_version=2,
    auth=('mjcollin', password_foreman))

fore.hosts.create(
    host={
        "name": "test.acis.ufl.edu",
        "ip":   "10.244.39.100",
        "mac":  "00:01:02:03:04:05",
        # try going back to name when interface works
        "hostgroup_id": "32",   # tried using *_name but didn't work, had to go 
                                # get id from database:
                                # select id,name,title from hostgroups;
        "architecture_name": "x86_64", # try removing when interface works
        "operatingsystem_name": "Ubuntu"# try removing when interface works
        }

)

#        "architecture_name": "x86_64",
#        "operatingsystem_name": "Ubuntu"
