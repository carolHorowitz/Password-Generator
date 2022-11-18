import random


def password_generator():
    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowcase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    simbols = ['!', '?', '#', '$', '%', '&', '(', ')', '*', '+', '{', '}']

    print("***********************************************")
    print("Welcome!! Let´s start to create a new password.")
    print("***********************************************")

    number_of_characters = int(input("How many character should there be?\n"))
    while number_of_characters < 4 or number_of_characters > 10:
        print("You must enter a number between 4 and 10.")
        number_of_characters = int(input("How many character should there be?\n"))


    pass_letters = str(input("Should it have uppercase letters? Answer Y or N\n").strip().upper())
    while pass_letters != "Y" and pass_letters != "N":
        print("You must enter Y or N.")
        pass_letters = str(input("Should it have uppercase letters? Answer Y or N\n").strip().upper())

    pass_numbers = str(input("Should it include numbers and special characters? Answer Y or N\n").strip().upper())
    while pass_numbers != "Y" and pass_numbers != "N":
        print("You must enter Y or N.")
        pass_numbers = str(input("Should it include numbers and special characters? Answer Y or N\n").strip().upper())

    pass_simbols = str(input("Should it have simbols? Answer Y or N\n").strip().upper())
    while pass_simbols != "Y" and pass_simbols != "N":
        print("You must enter Y or N.")
        pass_simbols = str(input("Should it have simbols? Answer Y or N\n").strip().upper())

    if pass_letters == "Y" and pass_numbers == "Y" and pass_simbols == "Y":
        password_all = (uppercase_letters + lowcase_letters + numbers + simbols)
        password = password_list(password_all, number_of_characters)

    elif pass_letters == "N" and pass_numbers == "Y" and pass_simbols == "Y":
        password_all = (lowcase_letters + numbers + simbols)
        password = password_list(password_all, number_of_characters)

    elif pass_letters == "N" and pass_numbers == "N" and pass_simbols == "Y":
        password_all = (lowcase_letters + simbols)
        password = password_list(password_all, number_of_characters)

    elif pass_letters == "N" and pass_numbers == "N" and pass_simbols == "N":
        password_all = (lowcase_letters)
        password = password_list(password_all, number_of_characters)

    elif pass_letters == "Y" and pass_numbers == "Y" and pass_simbols == "N":
        password_all = (lowcase_letters + uppercase_letters + numbers)
        password = password_list(password_all, number_of_characters)

    elif pass_letters == "Y" and pass_numbers == "N" and pass_simbols == "N":
        password_all = (lowcase_letters + uppercase_letters)
        password = password_list(password_all, number_of_characters)

    print("##################################")
    print('Your new password is: ' + password)
    print("##################################")

def password_list(password_all, number_of_characters):
    password = "".join(random.sample(password_all, number_of_characters))
    return password


if __name__ == "__main__":
    password_generator()
