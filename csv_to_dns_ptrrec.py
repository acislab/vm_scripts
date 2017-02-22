#!/usr/bin/python3
#
# Take CSV and print out DNS A records for the Bind zone file

import fileinput

for line in fileinput.input():
    machine = line.rstrip().split(",")
    print("{0}      in  ptr    {1}.".format(
        machine[2].split(".")[3], machine[0]))