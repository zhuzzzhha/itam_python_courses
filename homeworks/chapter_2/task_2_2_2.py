m={}
def some_obscure_function(s):
    for x in s:
        if type(x)==str:
            for i in range(len(x)):
                m[x[i]]=m.get(x[i],0)+1
        else:
            some_obscure_function(x)
    return m
a = ["wow", ["waow", "1000-7", "wahoo", ["oh"], ["dead", ["inside"]]]]
result = some_obscure_function(a)
print(result)
