# if elif else ...

arr = [[1, 2, 3], [4, 5, 6]]

for x, y, z in arr:
    print(x, y, z)

# enumerate - повертає ітератор та елемент послідовності

a = [1, 3, 5, 7, 9]
b = [0, 2, 4, 6, 8]

for i in enumerate(a):
    print(i[1])

for k, x in zip(b, a):
    print("k = %d, x = %d" % (k, x))

# до for/while циклу можна додавати else конструкцію, що виконається, якщо
# не виконається жодної ітерації в циклі або в кінці циклу

while a[0] == 1:
    print("hello")
    a[0] = 0
else:
    print("There no iterations")

# while/for цикли підтримують оператори break/continue
