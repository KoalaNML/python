import inflect
p = inflect.engine()

mylist = []
while True:
    try:
        name = input("Name: ")
        mylist.append(name)
    except EOFError:
        print()
        print("Adieu, adieu, to " + p.join(mylist))
        break