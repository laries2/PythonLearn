a = [3, 20, 42]
a.append(59)

a.pop()
print(a[2])


fruits = ["banana", "apple", "mangoes"]
temp = fruits[0]
fruits[0]=fruits[2]
fruits[2]=temp

print(fruits)



b=[1,3,5,7,9,11]
#c=[2,6,10,14,18,22]
c=[]
print(c)

for nums in b:
    c.append(nums*2)
print(c)