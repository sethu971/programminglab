print("simple calculator")
num1 = float(input("enter first number:"))
operator = input("enter operations:")
num2 = float(input("enter second number:"))
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = "error: invalid operator"
print ("result:",result)
