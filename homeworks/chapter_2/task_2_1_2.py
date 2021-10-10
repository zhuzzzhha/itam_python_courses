def summation(s):
    max=0
    sum=0
    for i in range(len(s)):
        if s[i]<0:
            s[i]*=(-2)
            if s[i]>max:
                max=s[i]
    for x in s:
       sum=sum+x/max
    print(sum)
s=list(map(int, input().split()))
summation(s)
