# printing 1 to 9
for i in range(1,10):
    print(i)
print("......................")


#using whole loop
a=0
sum=0
while a<10:
    # a=a+1
    a+=1
    sum+=a
print(sum)


#accesing lists
print(".........lists........")
lists=[2,4,1,6,9,-2,-6]
sum=0
i=0
while lists[i]>0:
    sum=sum+lists[i]
    i+=1
print(sum)

#for loop serving the same purpose as the above code
ss=0
for s in lists:
    if s>0:

        ss = ss + s
print(ss)

