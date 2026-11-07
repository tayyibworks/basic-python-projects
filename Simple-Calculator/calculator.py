#simple_calculator
num1=float(input("Enter the first number:"))
operator=input("Enter an operator (+,-,*,/):")
num2=float(input("Enter the second number:"))

if operator=='+':
    result=num1+num2
    print("Result of addition:",result)

elif operator=="-":
    result=num1-num2
    print("Result of subtraction:",result)

elif operator=="*":
    result=num1*num2
    print("Result of multiplication:",result)

elif operator=="/":
    if num2!=0:
        result=num1/num2
        print("Result of division:",result)
    else:
        print("Error:cannot be divided by 0")
else:
    print("Error:Invalid operator")
