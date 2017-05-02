# exceptions

# raise - генерувати виключення (без параметрів - повторна генерація виключення (аналог throw C++))
# except - теж що і catch C++

try:
    f = open("DatTypes.py", 'r')
except IOError as exceptions:
    print(exceptions)
except NameError as exceptions:
    print(exceptions + " File not found")

# кілька типів вийнятків можна перехопити так:
# except(IOError, NameError) as exceptions:
# except: - ця конструкція дозволяє перехобити будь-які типи вийнятків
# except Exception as e: - перехопити всі вийнятки, крім тих, що ведуть до
# негайного виходу з програми


for line in f:
    print(f.readline())

f.close()