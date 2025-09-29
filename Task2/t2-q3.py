def hash():
    string=input("enter numbers sepereated by space: ")
    numbers=[]
    for i in string.split():
        i=int(i)
        numbers.append(i)
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
    while low <= high:
        mid=(high+low)//2
        if sublist[mid] < num:
            low=mid+1
        else:
            high=mid
    return low
    
hash()