while True:
    try:
        fraction = input("Fraction: ")
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)
        result = round(x/y *100)
        if 99 <= result <= 100:
            print("F")
            break
        elif result <= 1:
            print("E")
            break
        elif result > 100:
            pass
        else:
            print(f"{result}%")
            break
    except (ValueError, ZeroDivisionError):
        pass
