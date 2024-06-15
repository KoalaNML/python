import sys
import csv

def main():
    check_arg()
    list = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last,first = row['name'].split(",")
                list.append({"first":first.lstrip(), "last":last, "house":row["house"]})
        with open(sys.argv[2], 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            for row in list:
                writer.writerow(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

def check_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()  