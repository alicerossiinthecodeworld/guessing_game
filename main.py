import random
from businesslogic import str_to_int_validate, yes_no_checker, check_the_number, greetings


name = input(f"Enter your name:\n")
correct_answer = random.randint(0, 100)
yes_no_checker(input(f"Hi, {greetings(name)}! wanna play a game?\n"))
check_the_number(str_to_int_validate(input(f"Enter your number:\n")), correct_answer)