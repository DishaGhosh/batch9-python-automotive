#def cal ():
#     def add(a, b):
#         return a + b
#     def sub(a, b):
#         return a - b
#     def mul(a, b):
#         return a * b
#     def div(a, b):
#          if b == 0:
#             return "Error: Cannot divide by zero"
#          return a / b
#     print("Simple Python Calulator")
#     print("Choose operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     choice = input("Enter choice (1/2/3/4): ")
#     if choice not in ["1", "2", "3", "4"]:
#         return "Invalid choice!"
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     if choice == "1":
#         return f"result: {add(num1, num2)}"
#     elif choice == "2":
#         return f"Result: {subtract(num1, num2)}"
#     elif choice == "3":
#         return f"Result: {multiply(num1, num2)}"
#     elif choice == "4":
#         return f"Result: {divide(num1, num2)}"
# print(cal())


# text = input("Enter a string: ")

# vowels = "aeiouAEIOU"
# count = 0

# for char in text:
#     if char in vowels:
#         count += 1

# print("Number of vowels:", count)



# my_list=[13,45,67,8,4,81]
# print("original list:",my_list)
# my_list.sort()
# print("sorted list :",my_list)


# my_list=[8,4,67,8,4,81,8,3,3]
# print("original list:",my_list)
# unique = set(my_list)
# print("unique_list",unique)

# num = int(input("enter the num:"))
# factorial = 1
# if num<0:
#     print("factorial doesnot exist")
# else:
#     for i in range(1, num+1):
#        factorial = factorial*i
# print(factorial)

# fibbonaci series:

num = int(input("enter the num:"))
a = 0
b = 1 
for i in range (num):
    print (a)
    print (b)
    c = a+b
    print(c)
    a=b
    b=c
num = int(input("enter the num :"))
if num % 2 == 0:
    print("the num is even")
else:
    print(" the num is odd")


a = 10
b = 3
print ("a/b =",a/b)
print("a//b =",a//b)
print("a % b =",a % b)
print("a * b =",a * b)
print("a + b =",a+b)
print("concatination =",a+b)
print("a*b=",a*b)

# armstrong number   153 = 1^3 +5^3 +3^3 =153
# num =  int(input("enter the num :"))
# temp = num
# sum = 0
# while temp>0:
#     digits = temp % 10
#     sum = sum + (digits**3)
#     temp = temp // 10
# if sum == num:
#     print("its armstring number")
# else:
#     print("its not armstrong number")




