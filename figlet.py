import pyfiglet
import sys
from random import choice

list = pyfiglet.FigletFont.getFonts()
try:
    if len(sys.argv) < 2:
        input = input("Input: ")
        figlet = pyfiglet.Figlet(font=choice(list))
        print("Output:\n",figlet.renderText(input))
    elif len(sys.argv) < 4:
        if sys.argv[1] in ['-f','--font'] and sys.argv[2] in list:
            input = input("Input: ")
            figlet = pyfiglet.Figlet(font=sys.argv[2])
            print("Output:\n",figlet.renderText(input))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
except pyfiglet.FontNotFound:
    sys.exit("Invalid usage")