def mod_div(fun):
    def inner(a, b):
        print("I am going to divide", a, "and", b , end = ' division is : ')
        if a < b:
              a, b = b, a
        
        return fun(a, b)
    return inner


@mod_div
def div(a, b):
    return a // b

a, b = (int(i) for i in input('Enter two values: ').split())
div(a, b)