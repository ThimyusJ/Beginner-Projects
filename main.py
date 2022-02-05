num1 = float(input("Enter A Number: "))
num2 = float(input("Enter A Second Number: "))
op = input("Enter An Operator: ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Operation Not Supported")

