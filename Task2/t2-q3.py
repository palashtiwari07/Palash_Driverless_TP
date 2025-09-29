def hash():
    n=int(input("enter the number of integers:"))
    numbers=[]
    print("enter the integers:")
    for i in range(n):
        num=int(input())
        numbers.append(num)
    hash_table=[]
    hash_table = [None]*10
    for row in range(10):
        hash_table[row] = []
    for num in numbers:
        index = num % 10
        sublist = hash_table[index]
        pos = binary_search(sublist,num)
        sublist.insert(pos,num)

    index=0
    for sublist in (hash_table):
        print("Index =",index,'--',sublist)
        index+=1

def binary_search(sublist, num):
    low=0
    high=len(sublist)-1
    while low < high:
        mid=(high+low)//2
        if sublist[mid] < num:
            low=mid+1
        else:
            high=mid
    return low
    
hash()