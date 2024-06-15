from tabulate import tabulate
import sys
import csv

def main():
    menu = []
    check_arg()
    try:
        with open(sys.argv[1], newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(row)

        print(tabulate(menu,headers='keys', tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

def check_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()  