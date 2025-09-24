class Cl:
    def sortf(self, strings):
        n=len(strings)
        for i in range(n):
            mini=i
            for j in range(i + 1, n):
                if strings[j] < strings[mini]:
                    mini=j
            strings[i], strings[mini] = strings[mini], strings[i]
        return strings

n = int(input("enter the number of strings"))
print("enter strings")
strings = []
for i in range(n):
    l = input()
    strings.append(l)

obj = Cl()
sorted_strings = obj.sortf(strings)
print(sorted_strings)