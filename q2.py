class Cl:
    def sortf(self, strings):
        n = len(strings)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if strings[j] < strings[min_idx]:
                    min_idx = j
            strings[i], strings[min_idx] = strings[min_idx], strings[i]
        return strings

n = int(input("Enter the number of strings: "))
print("Enter strings:")
strings = []
for i in range(n):
    l = input()
    strings.append(l)

obj = Cl()
sorted_strings = obj.sortf(strings)
print("Sorted strings:", sorted_strings)