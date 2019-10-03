n=2
power=0
l=[20,19]
l.sort()
a=0
for i in range(n):
    print(l[i])
    a+=(2**power)*l[i]
    p+=1
print(a-1)    