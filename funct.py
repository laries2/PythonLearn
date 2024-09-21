def function():
    print("the function")


print("Outside code")
function()


# mapping
def funct(x):
    return 2 * x


a = funct(5)
print(a)


def funct1(x, y):
    return x + y


b = funct1(2, 3)
print(b)


def funct2(x):
    print(x)
    print("Still on function")
    return 3 * x


c = funct2(4)
print(c)


def student_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}")


student_name("Hillary","Bett")
