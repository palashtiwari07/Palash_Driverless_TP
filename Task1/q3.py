class Cl():
    def searchf(self, strings, key):
        n=len(strings)
        low=0
        high=n-1
        while low <= high:
            mid=(low+high)//2     
            if strings[mid]==key:
                return mid
            elif strings[mid]<key:
                low=mid+1
            else:
                high=mid-1
        return -1

n = int(input("enter the number of strings: "))
print("enter strings")
strings = []
for i in range(n):
    l = input()
    strings.append(l)
key = input("enter the string to be searched")
strings.sort()

obj = Cl()
index = obj.searchf(strings, key)
if index == -1:
    print("string not found")
else:
    print("string found at index", index)
