def conc(**kwargs):
    result = ""
    # iterate over the keys of the python kwargs dic
    for x in kwargs.values():
        result += x
    return result
print(conc(a="My", b="Name", c="is", d="suraj", e="!"))
