def main():
    mealTime = input("What time is it? ")
    convertedTime = convert(mealTime) 
    if convertedTime >= 7 and convertedTime <= 8:
        print("breakfast time")

    elif convertedTime >= 12 and convertedTime <= 13:
        print("lunch time")

    elif convertedTime >= 18 and convertedTime <= 19:
        print("dinner time")

def convert(time):
    splittime = time.split(":")
    hours = float(splittime[0])
    minutes = float(splittime[1])
    newTime = hours + minutes/60
    return newTime

if __name__ == "__main__":
    main()