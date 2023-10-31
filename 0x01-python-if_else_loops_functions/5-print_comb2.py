#!/usr/bin/python3
for number in range(0, 100):
    spretor = ", "
    if number == 99:
        spretor = "\n"
    print("{:02d}".format(number), end=spretor)
