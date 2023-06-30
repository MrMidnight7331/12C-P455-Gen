#12C-Password-Generator
#By: MrMidnight / Twtiter: @MrMidnight53

import secrets
import string


def print_logo():
    print(" __   _____  _____      ______                    _____            ")
    print("/  | / __  \/  __ \     | ___ \                  |  __ \           ")
    print("`| | `' / /'| /  \/_____| |_/ /_ _ ___ ___ ______| |  \/ ___ _ __  ")
    print(" | |   / /  | |  |______|  __/ _` / __/ __|______| | __ / _ \ '_ \ ")
    print("_| |_./ /___| \__/\     | | | (_| \__ \__ \      | |_\ \  __/ | | |")
    print("\___/\_____/ \____/     \_|  \__,_|___/___/       \____/\___|_| |_|")
    print("By: MrMidnight // Twtiter: @MrMidnight53\n")


def generate():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    length = 8

    passwd1 = ""
    passwd2 = "-"
    passwd3 = "-"
    passwd4 = ""
    passwd5 = "-"

    passw = letters + digits
    for i in range(length):
        passwd1 += "".join(secrets.choice(passw))
        passwd2 += "".join(secrets.choice(passw))
        passwd3 += "".join(secrets.choice(passw))
        passwd5 += "".join(secrets.choice(passw))

    for i in range(length):
        passwd4 += "".join(secrets.choice(special_chars))

    print(passwd1  + passwd2 + '-"' + passwd4 + '"' + passwd5 + passwd3)

def __init__():

    try:
        num_inp = int(input("How many 12C-Passwords?: "))
    except ValueError:
        print("NOT A VALID VALUE!\n")
        __init__()


    for i in range(num_inp):
        print("Your password is:", end=" ")
        generate()

    print("\nGenerated!")
    exit()


print_logo()
__init__()