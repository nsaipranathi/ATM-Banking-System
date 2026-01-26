fruits=["apple", "banana", "graps", "orange"]
print (fruits[0:1])
print (fruits[-1])
print (fruits[1:3])
print("Number of fruits:", len(fruits))

fruits[2] = "pear"
print(fruits)

if "apple" in fruits:
    print("Apple is present in the list")
else:
    print("Apple is not present in the list")

fruits.remove("banana")
fruits.pop()
print(fruits)

fruits1=["watermelon","kiwi"]

fruits.extend(fruits1)
print(fruits)
n = len(fruits)

for i in range(n):
    for j in range(i + 1, n):
        if fruits[i] > fruits[j]:
            fruits[i], fruits[j] = fruits[j], fruits[i]

print("Sorted list:", fruits)
    

       

