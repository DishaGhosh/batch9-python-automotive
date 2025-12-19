print("Get max ,min swap value of variable")
print("\n 1. Max \n  2. Min  \n 3. Swap")
a,b = map (int ,  input ("enter 2 num:").split(",")) #34 , 23
choice = int (input("enter your choice"))
if (choice == 1):
    print(max(a,b))
elif(choice == 2):
    print(min(a,b))
elif(choice==3):
    a,b = b,a
    print("after swaping %d %d" %(a,b))  #23, 34
else:
    print("invalid choice")


while True:
    name = input("Enter your name: ")
    if name != "":
        break

    phone_number = "123-456-7890"


for i in phone_number:
    if i == "-":
        continue
    print(i, end=" ")


for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)