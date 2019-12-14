#!/usr/bin/env python3

print("Hello World")

def post_code_gen(x: str, y: str):

    x = x.split("-")
    x = ''.join(x)
    x = int(x)

    y = y.split("-")
    y = ''.join(y)
    y = int(y)


    generated_post_codes = []

    for post_code in range(x, y + 1):
        generated_post_codes.append(post_code)
        print ('%02d-%03d' % (post_code/1000, post_code%1000))

post_code_gen("79-900", "80-155")

