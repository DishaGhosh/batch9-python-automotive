# class interestcalculating:

#     def __init__(self,principal,rate,time,age):    # constructor 
#         self.principal = principal
#         self.rate = rate                       # store inside the object
#         self.time = time
#         self.age = age

#     def simple_interest(self):
#         SI = (self.principal * self.rate* self.time)/100
#         return SI
    
#     def compound_interest(self):
#         if self.age >=60:
#             rate = 8
#         else:
#             rate = 6
#         amount = self.principal * (1 + rate/100) ** self.time
#         CI = amount - self.principal
#         return CI
    
# try:          #used for ecception handling
#     p = float(input("enter the primcipal amount : "))
#     t = float(input("enter time :"))
#     r = float(input("enter the rate of interest:"))

#     ag = int(input("enter the age:"))

# # object creation
#     object1 = interestcalculating(p,r,t,ag)
#     print("simple interest :",object1.simple_interest())    # call the simple interest function and print

#     print("compound interest:",object1.compound_interest())   #  call the compound interest function and print

# # it will run only when the user enters wrong value
# except ValueError:
#     print("please enter valid number only.")
# finally:
#     print("done")


# i = 1
# while i <= 10:
#     print(3*i)
#     i += 1

