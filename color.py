# from termcolor import colored as col

# text =col("Hi there..!!", color="green")
# print(text)
from pyfiglet import figlet_format

from colorama import init
from termcolor import colored
init()
valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

# use Colorama to make Termcolor work on Windows too

# then use Termcolor for all colored text output
# text =colored('Hello, World!', 'white', 'on_red', attrs=['blink'])
# print(text)

msg = input("What would you like to to print..?")
color_choice = input("What color..?")
if color not in valid_colors:
    color = "magenta"
ascii_art = figlet_format(msg)
colored_ascii = (ascii_art, color=color_choice)
print(colored_ascii)
