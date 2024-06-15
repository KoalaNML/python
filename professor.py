import random

def main():
    level = get_level()
    round = 0
    score = 0
    while round < 10:
        x,y = generate_integer(int(level))
        result = x+y
        answer = input(f"{x} + {y} = ")
        if str(result) == answer:
            score += 1
        else:
            tries = 0
            while tries < 2:
                print("EEE")
                answer = input(f"{x} + {y} = ")
                if str(result) == answer:
                    tries = 2
                    score += 1
                tries += 1
            if answer != str(result):
                print("EEE")
                print(f"{x} + {y} = {result}")
        round += 1

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = input("Level: ")
            if int(level) in [1,2,3]:
                break
            else:
                pass
        except ValueError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    
    return x,y

if __name__ == "__main__":
    main()

