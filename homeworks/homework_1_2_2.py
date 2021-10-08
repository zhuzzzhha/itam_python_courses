och=0
zaoch=0
unknown=0
n=int(input())
for i in range(n):
    k=0
    a=input().split()
    for i in range(3):
        if a[i]=="True" or a[i]=="False":
            boolean=a[i]
            k=k+1
    if k>1:
        if a[i]=="True":
            och=och+1
        elif a[i]=="False":
                zaoch=zaoch+1
        else:
            unknown=unknown+1
    if k==1:
        if boolean=="True":
            och=och+1
        else:
            zaoch=zaoch+1
    else:
        unknown=unknown+1        
print("Очных - ", och,"Заочных - ", zaoch,"Неизвестных - ", unknown)
