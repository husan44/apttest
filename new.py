#! /usr/bin/env python3

import readline, sys
print("Enter characters")
# aaa
out_of = int(sys.argv[1])
while 1:
    line = input()
    total = 0
    for num in line.split(" "):
        total += int(num)
    print("Total: %d (%f%%)" % (total, total * (100 / out_of)))

