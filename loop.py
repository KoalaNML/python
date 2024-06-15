import pyfiglet
from random import choice
#test

list = pyfiglet.FigletFont.getFonts()
input = input("Input: ")
figlet = pyfiglet.Figlet(font=choice(list))
print("Output:",figlet.renderText(input))