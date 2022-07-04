lst = []

n = int(input("Enter number of elements: "))

for i in range(0, n):
    ele = input("Enter value: ")

    lst.append(ele)

tup1=tuple(lst)
print(lst)
print(tup1)
