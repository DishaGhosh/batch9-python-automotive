fruit =["banana", "apple","grapes", "orange"]

print(fruit[0])
print(fruit[3])

fruit[0]= "blueberry"
print(fruit[0])

fruit.append("guava")
fruit.remove("grapes")
fruit.pop()
fruit.pop(1)
fruit.insert(1,"jackfruit")
fruit.sort()
fruit.clear()

for i in fruit:
    print(i)
