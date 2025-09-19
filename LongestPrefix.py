#find longest common prefix from given list of string
def Find_prefix(data):
    prefix=data[0]
    for d in data[1:]:
        while not d.startswith(prefix):
            prefix=prefix[:-1]
        if prefix=="":
            return ""
    return prefix
print(Find_prefix(["flower","flow","flight"]))
