#!/usr/bin/env python3
def palindrome(s):
    return s == s[::-1]
if __name__ == '__main__':
    s = input("string: ")
    if palindrome(s):
        print("yes")
    else:
        print("no")

