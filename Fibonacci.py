#!/usr/bin/env python3
a, b = 0, 1
while b < 100:
    print(b)
    import pdb; pdb.set_trace()
    a, b = b, a + b

