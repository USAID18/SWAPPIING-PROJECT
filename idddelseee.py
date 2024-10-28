height=float(input("enter your height in cm:"))
weight=float(input("enter you wieght in kg:"))


bmi=weight/(weight/100)**2
if bmi<= 19.8:
    print("youre under wieght")

elif bmi<= 20.1:

    print("youre healthy")


else:
    print("youre obese")
