# from termcolor import colored as col

# text =col("Hi there..!!", color="green")
# print(text)

from colorama import init
from termcolor import colored
 
# use Colorama to make Termcolor work on Windows too
init()
 
# then use Termcolor for all colored text output
print(colored('Hello, World!', 'green', 'on_red'))