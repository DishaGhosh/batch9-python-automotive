def phy(score):
    return score >= 60

marks = float(input("enter the marks in physics :"))

if phy(marks):
    print("pass")
else:
    print("fail")