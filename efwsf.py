n=int(input(""))
x=list(map(int,input("").split()))
x.sort()
m=[]
for i in range(len(x)-1):
    if x[i]==x[i+1] and x[i] not in m:
        m.append(x[i])
if (m):
    for i in m:
        print(i)
else:
    print("unique")
