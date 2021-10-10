def product(a, b):
    if a < 0:
        a *= -1
    elif b < 0:
        b *= -1
    result = a * b
    print("Product of", a, "and", b, "equals", result)
    return result
def pre_product(a,b):
    if type(a)!=int and type(b)!=int:
        a=int(a)
        b=int(b)
        product(a,b)
    else:
        product(a,b)
