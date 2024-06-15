import sys
i=0
try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

    with open(sys.argv[1]) as file:
        for _ in file:
            if not _.lstrip().startswith("#") and not _.isspace():
                i+=1
    
    print(i)
except FileNotFoundError:
    sys.exit("File does not exist")
