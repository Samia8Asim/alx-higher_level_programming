#!/usr/bin/python3

for code in range(ord('z'), ord('a') - 1, -1):
    print(
        "{}".format(chr(code)) if (code % 2) == 0
        else "{}".format(chr(code - 32)),
        end=""
    )
