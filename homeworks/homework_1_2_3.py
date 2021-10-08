
def split(s):
    return [char for char in s]
a=input()
b=split(a)
n=len(b)
f=False
for i in range(n):
    if b[i].isupper():
        j=i
    if b[i].isdigit() and f==False:
        k=i+1
        f=True
b=b[j:n:k-j]
print(" ".join(b))
