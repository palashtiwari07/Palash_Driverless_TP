n=int(input("enter the number of strings"))
print("enter strings")
strings=[]
for i in range(n):
    l=input()
    strings.append(l)
d={}
for i in strings:
    for k in i:
        if k in d:
            d[k]+=1
        else:
            d[k]=1
print(d)