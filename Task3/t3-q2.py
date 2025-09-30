import csv
f = open(r"C:\Formula_Taskphase\Task3\names.csv", "r")
reader=csv.reader(f,skipinitialspace=True)
    
data=list(reader)
sorted_data=sorted(data,key=lambda x: x[0])
print("sorted data is")
for i in sorted_data:
    print(i)
print("\n")

for i in sorted_data:
    if int(i[0]) % 2 != 0:
        sorted_data.remove(i)  

print("data after removing rows is")
for i in sorted_data:
    print(i)
print("\n")

for i in sorted_data:
    i[1]=i[1].strip()

string = ""
for i in sorted_data:
    string += i[1]
print(string)