# region Imports
import string

# endregion


# region Program Functions
def initialize_pencil_count():
    print("How many pencils would you like to use:")
    pencil_count = 0
    valid_count = False
    while not valid_count:
        try:
            pencil_count = int(input())
        except ValueError:
            print("The number of pencils should be numeric")
            continue
        if int(pencil_count) < 1:
            print("The number of pencils should be positive")
            continue
        valid_count = True
    pencil_count = int(pencil_count)
    pencil_string = ""
    for i in range(pencil_count):
        pencil_string += "|"
    return pencil_string


def set_player_numbers():
    player_one = input("Who will be the first (Joachim, Anna):")
    while (player_one != "Joachim") and (player_one != "Anna"):
        player_one = input("Choose between 'Joachim' and 'Anna'")
    if player_one == "Joachim":
        player_two = "Anna"
    else:
        player_two = "Joachim"
    return player_one, player_two


def play_game(pencils, player_list):
    turn_counter = len(pencils)
    player_one = player_list[0]
    player_two = player_list[1]
    current_player = player_one
    while turn_counter >= 1:
        num_to_strip = ""
        print(pencils)
        if current_player == "Joachim":
            print(f"{current_player}'s turn!")
        else:
            print(f"{current_player}'s turn:")
        if current_player == "Anna":
            if len(pencils) == 1:
                num_to_strip = "1"
                print("1")
            elif len(pencils) == 2:
                num_to_strip = "1"
                print("1")
            elif len(pencils) == 3:
                num_to_strip = "2"
                print("2")
            elif len(pencils) % 4 == 0:
                num_to_strip = "3"
                print("3")
            elif (len(pencils) + 1) % 4 == 0:
                num_to_strip = "2"
                print("2")
            elif (len(pencils) + 2) % 4 == 0:
                num_to_strip = "1"
                print("1")
            else:
                num_to_strip = "3"
                print("3")
        else:
            num_to_strip = input()
        valid_count = False
        while not valid_count:
            while not str(num_to_strip.isdigit()):
                num_to_strip = input("Possible values: '1', '2', or '3'")
                continue
            if str(num_to_strip) not in string.digits:
                num_to_strip = input("Possible values: '1', '2', or '3'")
                continue
            if int(num_to_strip) < 1 or int(num_to_strip) > 3:
                num_to_strip = input("Possible values: '1', '2', or '3'")
                continue
            if int(num_to_strip) > len(pencils):
                num_to_strip = input("Too many pencils were taken")
                continue
            break
        num_to_strip_to_neg = -abs(int(num_to_strip))
        num_to_slice = slice(num_to_strip_to_neg)
        pencils = pencils[num_to_slice]
        turn_counter = len(pencils)
        if current_player == player_one:
            current_player = player_two
        else:
            current_player = player_one
        if turn_counter == 0:
            print(f"{current_player} won!")


# endregion


# region Main program execution
number_of_pencils = initialize_pencil_count()
players = set_player_numbers()
play_game(number_of_pencils, players)
# endregion
