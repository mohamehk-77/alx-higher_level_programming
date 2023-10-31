#!/usr/bin/python3
for a in range(0, 9):
    for b in range(a+1, 10):
        spertor = ", "
        if a == 8:
            spertor = "\n"
        print("{:d}{:d}".format(a, b), end=spertor)
