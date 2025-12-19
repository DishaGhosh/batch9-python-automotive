# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     if b == o:
#         return "cannot divide by zero"
#     else:
#         return a/b
    
# num1 = int(input("enter the 1st num :"))
# num2 = int(input("enter the 2nd num:"))

# print("Choose operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")
    
# choice = int(input("enter the choice :"))

# if choice == "1":
#     print("result:", add(num1,num2))

# elif choice == "2":
#     print("result :", sub(num1,num2))

# elif choice == "3":
#     print("result :", mul(num1,num2))

# elif choice == "2":
#     print("result :", div(num1,num2))

# else:
#     print("invalid choice")


def phy(score):
    return score > 60

marks = int(input("enter the marks in physics :"))

if phy(marks):
    print("pass")
else:
    print("fail")


