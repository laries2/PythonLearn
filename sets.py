#Is a type of data that stores a set of unique things

a=[2,3,3,4,5,2,0,8,6,3,5]
print(a)
c=set()
print(c)

for values in a:
    c.add(values)
print(c)

for sets in c:
    a.append(sets)
print(a)

#find sum the unique elements
metrics = [1,3,4,1,3]
uniques= set()
total=0
for x in metrics:
    uniques.add(x)
for u in uniques:
    total+=u


print(uniques)
print(total)
