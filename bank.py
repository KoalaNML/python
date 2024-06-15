greeting = input("Greeting: ").strip().lower()
if "hello" in greeting :
    money = "$0"

elif greeting[:1] == "h" and not greeting == "hello" :
    money = "$20"

else :
    money = "$100"

print(money)