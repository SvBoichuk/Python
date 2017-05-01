retPair = divmod(5, 2)

print("divmod = ", retPair)

# div = retPair[0]
# mod = retPair[1]

div, mod = retPair

# C - style print format???
# print("Div = %d, mod = %d", div, mod)
# All OK
print("Div = %d, mod = %d" % (div, mod))

total = sum(retPair)

print("Total = ", total)
print("Len = ", len(retPair))

array = [1, 2, 3, 4, 5, 6]

print("Seek ", array[1: 5: 2])

add2Arrys = list(retPair) + array

print("new arr = ", add2Arrys)


def PrintStringN(string, count):
    if count > 0:
        string *= count
    print(string)


count = int(input("Enter repeat count: "))
string = input("Enter string: ")

PrintStringN(string, count)

# При зрізах коли вказується крок зрізу, необхідно вважати на к-сть алементів з прававід знаку "="


formatedString = "Name: %s\nAge: %d" % ("Alan", 29)

print(formatedString)

eval_calc = eval("2+3")

print("Eval = ", eval_calc)


def min_val(a, b):
    return a if a < b else b

print("min from [%d,%d] is %d" % (4,5, min_val(4,5)) )

# подивитися до генераторів списків

var = [x if x > 4 else (x*2) for x in array]

