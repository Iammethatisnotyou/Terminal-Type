import random
import os
import glob
import subprocess, sys

two_hundred_common_dir = "/home/LiamUSR/programs/Python/typing_linux/words/two_hundred_common.txt"
two_hundred_text_dir = "/home/LiamUSR/programs/Python/typing_linux/words/two_hundred_common.txt"
def two_hundred(two_hundred_common_dir):
    try:
        with open(two_hundred_common_dir, "r") as file:
            list_file_content = file.read().split('\n')
            random.shuffle(raw_file_content := list(list_file_content))
            file_content = ' '.join(raw_file_content)
            print("list_file_content", list_file_content, "raw_file_content", raw_file_content, "file_content", file_content)
            return file_content

    except Exception as e:
        raise TypeError(f"Can't open file\n{e}")

def main():
    two_hundred(two_hundred_common_dir)

if __name__ == '__main__':
    main()
