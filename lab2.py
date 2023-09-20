list_nos = []
print("enter list of numbers")

for i in range(5):
    list_nos.append(int(input()))

print("sum is:", sum(list_nos))

avg=0
for i in range(5):
    avg += list_nos[i]

avg = avg / 5
print("Average is:", avg) 

# TASK 2

for i in range(-4, 1):
    print(list_nos[-i])