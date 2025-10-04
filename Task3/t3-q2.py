import csv
with open(r"C:\Formula_Taskphase\Task3\names.csv", "r") as f:
    reader=csv.reader(f,skipinitialspace=True)
    data=list(reader)

print("initial data is")
for row in data:
    print(row)
print("\n")

sorted_data=sorted(data,key=lambda x: int(x[0]))
print("sorted data is")
for row in sorted_data:
    print(row)
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

combined = ""
for i in sorted_data:
    combined += i[1]
print("all names combined",combined)

min_diff=200
for i in range(len(combined)-1):
    diff=abs(ord(combined[i]) - ord(combined[i+1]))
    if diff < min_diff:
        min_diff = diff
print("minimum absolute ascii difference is",min_diff)