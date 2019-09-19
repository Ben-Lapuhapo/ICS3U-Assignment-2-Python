#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: September 18 2019
# This program calculates volume of a circumference.
#  from user input


import math


def main():
    print("")
    radius = int(input("Enter the Circumference's Radius(mm): "))
    # output
    volume = (4/3*math.pi*radius**3)
    print("")
    print("Volume is {} mm^3".format(volume))


if __name__ == "__main__":
    main()
