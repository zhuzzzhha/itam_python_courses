s=input().split()
def summation(s):
    for i in range(len(s)):
        sum=0
        if s[i]<0:
            list(map(lambda x:x*(-2),s))
        sum+=s[i]
        return sum
print(summation(s))

