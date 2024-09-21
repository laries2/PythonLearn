fruits = ["banana", "apple", "mango"]
temp = fruits[0]
fruits[0]=fruits[2]
fruits[2]=temp

print(fruits)
# for loop to print each and every element in the list

for fruit in fruits:
    print(fruit)
    print(fruit)

deposits = [2550,600,7000]
balance = 0
for amount in deposits:
    balance = balance + amount

print("Total balance is :", balance)

a=list(range(0,10))
print(a)
total = 0
for num in a:
    total = total + num
print(total)
print("Multiples of both 3 and 5")
multiples = range(1,100)
for i in multiples:
    if i % 3 == 0 and i % 5 == 0:
        print(i)





