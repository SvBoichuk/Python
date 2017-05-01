retPair = divmod(5,2)

print("divmod = ", retPair)

# div = retPair[0]
# mod = retPair[1]

div, mod = retPair

# C - style print format???
print("Div = %d, mod = %d", div, mod)

total = sum(retPair)

print("Total = ", total)
print("Len = ", len(retPair))

array = [1,2,3,4,5,6]

print("Seek ", array[1 : 5 : 2])

add2Arrys = list(retPair) + array

print("new arr = ", add2Arrys)


def PrintStringN(string, count):
    if count > 0:
        string *= count
    print(string)


count = int(input("Enter repeat count: "))
string = input("Enter string: ")

PrintStringN(string, count)




