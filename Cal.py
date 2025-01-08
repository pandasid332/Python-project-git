print("Welcome to first program")
print("***************************************************")

a=float(input("Enter first value: "))
b= float(input("Ebter second value: "))

print("Enter any option from below: ")
print("***************************************************")
print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")
print("***************************************************")

c=int(input())

if c==1:
    print("addition of two value is: {}".format(a+b))
elif c==2:
    print("subtraction of two value is: {}".format(a - b))
elif c==3:
    print("multiplication of two value is: {}".format(a * b))
elif c==4:
    print("division of two value is: {}".format(a / b))
else:
    print("Enter correct option.")