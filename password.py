import string
import random

master_pwd = input("What is the master password? ")


def view():
    try:
        with open('password.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, password = data.split("|")
                print(f"Name: {user}, Password: {password}")
    except FileNotFoundError:
        print("No passwords stored yet. Please add some passwords first.")


def add():
    name = input("Enter name: ")
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    plen = int(input("Enter password length: "))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    generated_password = "".join(random.sample(s, plen))
    print("Your Password is:", generated_password)

    with open('password.txt', 'a') as f:
        f.write(name + "|" + generated_password + "\n")


while True:
    mode = input("Would you like to add a new password or view old ones (view, add), press q to quit: ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

