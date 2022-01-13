def str_to_int_validate(some_input: str) -> int:
    try:
        int(some_input)
    except ValueError:
        some_input = str_to_int_validate(input(f"Not a number. Enter number!\n"))
    return int(some_input)


def greetings(name: str = None):
    if name:
        return name
    return "anonymous"


def yes_no_checker(answer: str) -> bool:
    if answer == "yes":
        return True
    elif answer == "no":
        yes_no_checker(input(f"Think again\n"))
    else:
        yes_no_checker(input("Pls insert yes or no\n"))


def check_the_number(user_number: int, wanted_number: int) -> None:
    if user_number > wanted_number:
        new_user_number = input(f"try smaller\n")
        check_the_number(int(new_user_number), int(wanted_number))
    elif user_number == wanted_number:
        print(f"congrats!")
    else:
        new_user_number = input(f"try bigger\n")
        check_the_number(int(new_user_number), int(wanted_number))