list_nos = []
print("enter list of numbers")

for i in range(5):
    list_nos.append(int(input()))

print("sum is:", sum(list_nos))

# TASK 2

for i in range(-4, 1):
    print(list_nos[-i])