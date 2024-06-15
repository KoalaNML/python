grocery = {}
while True:
    try:
        item = input()
        grocery.setdefault(item, 0)
        grocery[item] += 1
    except EOFError:
        print()
        for _ in sorted(grocery):
            print(grocery[_], _.upper())
        break