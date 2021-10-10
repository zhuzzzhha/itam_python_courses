def debug_control(*args):
    kstr=0
    kbool=0
    kint=0
    kfloat=0
    if type(args)==str:
        kstr+=1
    if type(args)==int:
        kint=1
    if type(args)==float:
        kfloat+=1
    print("str:", kstr, "int:", kfloat, "float:", "bool:")
print(debug_control("Hello!", 1000, 7, 993.0, name="Petr", task="Eliminate"))
