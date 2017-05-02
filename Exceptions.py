# exceptions

# raise - генерувати виключення (без параметрів - повторна генерація виключення (аналог throw C++))
# except - теж що і catch C++

#f = open("DataTypes.py", 'r')

try:
     f = open("DataTypes.py", 'r')
except IOError as exceptions:
    print(str(exceptions) + "File not found!")
else: # виконується, якщо не було згенеровано вийнятку
    for line in f:
        print(f.read())
    f.close()

#finally: # використовується для завершення дії незалежно від того, чи було згенеровано вийняток
    #f.close() # не бачить f...???

# кілька типів вийнятків можна перехопити так:
# except(IOError, NameError) as exceptions:
# except: - ця конструкція дозволяє перехобити будь-які типи вийнятків
# except Exception as e: - перехопити всі вийнятки, крім тих, що ведуть до
# негайного виходу з програми

# розібратися з виключеннями і областю видимості!!!

#BaseException - базовий клас

with open("PillowLib.py") as f:
    for line in f.readlines():
        print(line)

# with - сама закриє файл в кінці!!!