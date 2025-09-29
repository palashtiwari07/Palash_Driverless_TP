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
        hash_table[index].append(num)
    
    index=0
    for sublist in (hash_table):
        print("Index =",index,'--',sublist)
        index+=1


hash()