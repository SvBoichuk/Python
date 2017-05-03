# Functions


def my_pwr_func(number, step=2):
    return float(number) ** float(step)


i = 1

while i < 5:
    print("%0.2f in step 2 = %0.2f" % (i, my_pwr_func(i)))
    i += 1

# занчення аргументів за замовч. зберігаються між викликами функцій!!!

def my_print(format_str, *args):
    print(format_str % args)

# * - довільна к-ксть аргументів
# присутні іменовані аргументи як в C#

print(my_pwr_func(step=4,number=2))

# пристуня можливість визначати вкладені функції!!!

var_a = 12

def func():
    var_a = 5
    print("var_a = ", var_a)

func()

print("var_a aft func = ", var_a)