#!/usr/bin/python3
#
# Take CSV and print out DNS A records for the Bind zone file

import fileinput

for line in fileinput.input():
    machine = line.rstrip().split(",")
    print("{0}      in  a    {1}".format(
        machine[1], machine[2]))