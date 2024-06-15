expression = input("Expression: ")
newEx = expression.split(" ")
x = float(newEx[0])
y = newEx[1]
z = float(newEx[2])
if y == "+":
    result = x + z

elif y == "-":
    result = x - z

elif y == "*":
    result = x * z

elif y == "/":
    result = x / z

print(f"{result:.1f}")