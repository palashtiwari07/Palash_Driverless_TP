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
        hash_table[index].append(num)
    
    index=0
    for sublist in (hash_table):
        print("Index =",index,'--',sublist)
        index+=1


hash()