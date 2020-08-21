def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result
print(my_sum(1,4,5))
