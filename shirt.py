import sys
from PIL import Image,ImageOps
from os.path import splitext

def main():
    check_arg()
    try:
        muppet = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet2 = ImageOps.fit(muppet, size)
    Image.Image.paste(muppet2, shirt, mask=shirt)
    muppet2.save(sys.argv[2])

def check_arg():
    file1 = splitext(sys.argv[1].lower())
    file2 = splitext(sys.argv[2].lower())
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not(sys.argv[1].endswith(('jpg','jpeg','png'))):
        sys.exit("Invalid input")
    if not sys.argv[2].endswith(('jpg','jpeg','png')):
        sys.exit("Invalid output")
    if file1[1] != file2[1]:
        sys.exit("Input and output have different extensions")

if __name__ == "__main__":
    main()  