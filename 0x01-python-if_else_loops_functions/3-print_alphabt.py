#!/usr/bin/python3
for alpha in range(ord('a'), ord('z') + 1):
    if alpha not in (ord('q'), ord('e')):
        print("{}".format(chr(alpha)), end='')
