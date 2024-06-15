vowels = ["a","e","i","o","u"]
text = input("Input: ")
print("Output: ",end="")
for letter in text:
    if letter.lower() not in vowels:
        print(letter,end="")

print()
