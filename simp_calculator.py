def add(x,y):
    return x + y
def substract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def division(x,y):
    if y == 0:
        return "Error divisio by 0"
    return x / y
print("select Operation")
print("+,-,*,/")

Operator = input("Seclect Operators(+,-,*,/): ")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

if Operator == "+":
    print(f"The Sum is: { add(num1 , num2)}")

elif Operator == "-":
    print(f"The substractions is: { multiply(num1 , num2)}")

elif Operator == "*":
    print(f"The Multiplications is: { substract(num1 , num2)}")

elif Operator == "/":
    print(f"The Division is:  { division(num1 , num2)}")
else:
    print("Invalid paramaters!")
