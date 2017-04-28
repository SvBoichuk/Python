# Python data types

def CompareObjects(a , b):
    if a == b:
        return "equal as data"
    elif a is b:
        return "equal as referense"
    elif type(a) is type(b):
        return "equal as data type"
    else: return "not equal"

a = 12
b = a

msg = CompareObjects(a,b)

print(msg)