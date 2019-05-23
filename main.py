x = int(input("Choose a number for tha value of x: "))
y = int(input("Choose a number for tha value of y: "))
operation = input("Choose the type of operation you want to do: ")
if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("Don't recognize the type of operation")