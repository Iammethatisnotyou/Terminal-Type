import os
import time
from datetime import datetime
import threading
from colorama import Fore, Back, Style
from pynput.keyboard import Key, Controller
from pynput import keyboard
import random
import glob

#from word_chooser import two_hundred eothueoaueoth

#two_hundred_common_dir = word_chooser.two_hundred_common_dir
#word_chooser.two_hundred(two_hundred_common_dir)
brown_fox = "The quick brown fox jumps over the lazy dog"
alphabet_lets = "abcdefghijklmnopqrstuvwxyz"
configuration_dir = "/home/LiamUSR/programs/Python/typing_linux/words/two_hundred_common.txt"
two_hundred_dir = "/home/LiamUSR/programs/Python/typing_linux/configuration.txt"
raw_text = brown_fox
text = list(raw_text)
correct_chars = 0
incorrect_chars = 0

def two_hundred():
    global file_content, raw_text, text
    try:
        with open(configuration_dir, "r") as file:
            list_file_content = file.read().splitlines()
            random.shuffle(raw_file_content := list(list_file_content))
            file_content = ' '.join(raw_file_content)
        raw_text = ' '.join(list_file_content)
        text = list(raw_text)

    except Exception as e:
        raise TypeError(f"Can't open file\n{e}")

def load_configuration():
    global raw_text, text
    with open(two_hundred_dir, 'r') as file:
        content = file.read().strip()
    if content == "200":
        try:
            print("it is correct")
            two_hundred()
        except Exception as e:
            raw_text, text = (brown_fox, list(brown_fox))
    elif content == alphabet_lets:
        raw_text = alphabet_lets
        text = list(raw_text)

def configuration(choice: str) -> None:
    with open (two_hundred_dir, 'w') as file:
        if choice == "200":
            file.write("200")
        elif choice == "alphabet":
            file.write(alphabet_lets)


class MyException(Exception): pass

def clear_and_print():
    print(chr(27) + "[2J")
    print(raw_text)
    print('\n')

def on_press():
    clear_and_print()
    start = datetime.now()
    while True:
        try:
            if hasattr('char') and key.char:  # Handle regular key presses
                print(key)
                t2 = threading.Thread(typing, args=(key.char))
                t2.start()
                #t2.join()

                return True
        except AttributeError:
                return False

        # Check if 'esc' is pressed to stop the listener
        if key == keyboard.Key.esc or key == keyboard.Key.tab:
            main()
            raise MyException("Escape key or tab was pressed")
    end = datetime.now()
    elapsed_time = (end - start).total_seconds()
    print(f"{elapsed_time}, seconds")
    

def typing():
    for char in text:
        with keyboard.Listener(on_press=on_press) as listener:
            key = listener.join()
            try:
                key == char
                clear_and_print(True, char[text])
            except MyException as e:
                print('{0} was pressed'.format(e.args[0]))

def choosing_text():
    print(f"Type \"200\" for 200 random words or type \"alphabet\" for abc's.")
    configuration_choice = input().lower()

    if configuration_choice == "200":
        print("200 random words chosen")
        configuration("200")
    elif configuration_choice == "alphabet":
        print("Alphabet text chosen")
        configuration("alphabet")
    elif len(configuration_choice.strip()) != 0:
        print(Fore.RED+"Invalid Choice, nothing being saved"+Style.RESET_ALL)

def main():
    load_configuration()
    print(raw_text, text)
    while True:
        print(f"Welcome what would you like to do?\n1: Type\n2: Save progress\n3: Exit")
        user_choice = input()
        if user_choice == '1':
            on_press()
        elif user_choice == '2':
            choosing_text()
        elif user_choice == '3':
            exit()
        else:
            print(Fore.RED+"Invalid Choice"+Style.RESET_ALL)

if __name__ == "__main__":
    main()

    t1 = threading.Thread(target=main)
    #t2 = threading.Thread(target, args)

    t1.start()
    #t2.start()

    t1.join()
    #t2.join()
