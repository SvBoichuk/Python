# Python data types


def CompareObjects(a, b):
    if a == b:
        return "equal as data"
    elif a is b:
        return "equal as referense"
    elif type(a) is type(b):
        return "equal as data type"
    else:
        return "not equal"

a = 12
b = a

print("a = ", a)
print("b = ", b)

b = 4

print("after")
print("a = ", a)
print("b = ", b)

msg = CompareObjects(a, b)

print(msg)
print(type(msg))

# isinstance - перевірка типу змінної (враховує наслідування)

# розрізняти копію змінної (обєкту від ссилки)

arr = [1,2,3]

aref = list(arr)

aref[2] = 0

print("aref = ", aref)

arr[0] = 12

print("aref2 = ", aref)

print("arr[2] = ",arr[2])

if isinstance(arr,list):
    arr.append(4)

print("arr = ", arr)

for a in arr:
    print(a**2)

import sys

var = sys.getrefcount(b)

print("var =", var)

# є 2 типи копіюваннь глибоке і поверхневе
# при поверхневому, створюються окремі обєкти що містять посилання на існуючі, що беруться з обєкту з якого виконується
# копіювання. При глибокому копіюванні - стрворюються повні нові копії (import copy; copy.deepcopy())

ar2 = [1,2,[3,4],5]
print("ar2 = ", ar2)
refArr2 = list(ar2)
print("refArr2 = ", refArr2)
refArr2[2][0] = 8
refArr2[0] = 9
print("After changes")
print("ar2 = ", ar2)
print("refArr2 = ", refArr2)

line = "Text,1024,25.5"
fieldTypes = [str, int, float]
rawFields = line.split(',')

fields = [typeOf(val) for typeOf, val in zip(fieldTypes,rawFields)]
# wtf?

print("Fields: ",fields)

arr.sort()

print("Sorted arr: ", arr)

string = "My name is {name}, and i'm {years} old!"

name = "Sviatoslav"
age = 21

formString = string.format(name = name, years = age)

print(formString)