#!/usr/bin/env python3
a = [20,23,45,56,]
a.append(110)
b = [45, 56, 90]
a.append(b)
print(*a, sep = ", ")

