a = [3, 20, 42]
a.append(59)

a.pop()
print(a[2])


fruits = ["banana", "apple", "mangoes"]
temp = fruits[0]
fruits[0]=fruits[2]
fruits[2]=temp

print(fruits)