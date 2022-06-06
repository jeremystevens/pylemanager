#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2022 Jeremy Stevens <jeremiahstevens@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining #a copy
# of this software and associated documentation files (the "Software"), #to deal
# in the Software without restriction, including without limitation the #rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or #sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be #included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, #EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF #MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR #OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, #ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER #DEALINGS IN THE
# SOFTWARE.
#
# ==============================================================================
version = "1.0.0"
# ==============================================================================

#    --- CHANGELOG: ----
#
#    Changes in: V1.0.0
#    -------------------
#  - recursively search for files by name
#  - recursively search for files by file type.
#  - copy files / backup files
#  - display directory tree
#  - Shred files (rewrite data to 0's)
#  - Get file info


# dependencies List:
#   - simple_term_menu
#   - art
#   - tqdm
#   - time
#   - os
#   - glob
#   - sys
#   - shutil

import shutil
import art as art
from simple_term_menu import TerminalMenu
from art import tprint
from art import *
import tqdm
import time
import os
import glob
import sys


# get file info function
def get_file_info(file_path):
    # get the file name
    file_name = os.path.basename(file_path)
    # get the file size
    file_size = os.path.getsize(file_path)
    # get the file creation date
    file_creation_date = time.ctime(os.path.getctime(file_path))
    # get the file last modified date
    file_last_modified_date = time.ctime(os.path.getmtime(file_path))
    # get the file last accessed date
    file_last_accessed_date = time.ctime(os.path.getatime(file_path))
    # get the file type
    file_type = os.path.splitext(file_path)[1]
    # get the file owner
    file_owner = os.path.split(os.path.split(file_path)[0])[1]
    # get the file group
    file_group = os.path.split(os.path.split(file_path)[0])[1]
    # get the file permissions
    file_permissions = oct(os.stat(file_path).st_mode)[-3:]
    # print the file info
    print("File Name: " + file_name)
    print("File Size: " + str(file_size))
    print("File Creation Date: " + file_creation_date)
    print("File Last Modified Date: " + file_last_modified_date)
    print("File Last Accessed Date: " + file_last_accessed_date)
    print("File Type: " + file_type)
    print("File Owner: " + file_owner)
    print("File Group: " + file_group)
    print("File Permissions: " + file_permissions)
    # ask if they want to return to main menu
    user_input = input("Would you like to return to the main menu? (y/n): ")
    # if the user input is yes
    if user_input == "y":
        # return to the main menu
        main()
    # if the user input is no
    elif user_input == "n":
        # exit the program
        sys.exit()
    # anything besides yes or no
    else:
        # if they can't answer a simple y/n question
        # just Quit the program because they are a moron
        sys.exit()


# shred file function rewrite data to 0's
def shred_file():
    tprint("Shred File", font="rnd-small")
    # enter full path and file name
    file_name = input("Enter the full path and file name: ")
    if os.path.exists(file_name):
        # confirm they really want to shred file
        confirm = input(f"Are you sure you want to shred {file_name}? (y/n): ")
        # if no then go back to more options menu
        if confirm == "n":
            more_options()
        # if not yes then continue
        with open(file_name, "r") as file:
            # read the file
            data = file.read()
            # write new random data to the file
            with open(file_name, "w") as file:
                # write 0's to the file
                file.write("0" * len(data))
            # rename the file
            os.rename(file_name, file_name + ".shred")
            # scond pass to write random unrecoverable data to the file
            with open(file_name + ".shred", "w") as file:
                # write random garbage data to the file
                file.write("001010102393929929394020" * len(data))
            # delete the file
            os.remove(file_name + ".shred")
            # print a message to the user
            print(f"{file_name} has been shredded")
    else:
        # if the file doesn't exist
        # print a message to the user
        print(f"{file_name} does not exist")
        more_options()


# function for more options
def more_options():
    tprint("More Options", font="rnd-small")
    options = ["Show Dir Tree", "Shred file", "Get File Info", "Go Back"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    if menu_entry_index == 0:
        # sudo display directory tree
        display_tree("/")

    elif menu_entry_index == 1:
        shred_file()

    elif menu_entry_index == 2:
        # get file info
        get_file_info()
    elif menu_entry_index == 3:
        # go back to main menu
        main()


# display interactive directory tree
def display_tree(path, indent=0):
    for entry in os.scandir(path):
        if entry.is_dir():
            print('{}[{}]'.format(' ' * indent, entry.name))
            display_tree(entry.path, indent + 2)
        else:
            print('{}- {}'.format(' ' * indent, entry.name))


def copy():
    tprint("Copy Files", font="rnd-small")
    source = input("Enter the source directory: ")
    destination = input("Enter the destination directory: ")
    copy_files(source, destination)


def copy_files(source, destination):
    # check if the source exists
    # save text for each file that was copied to a txt file
    # check if it exists and if not create it
    if os.path.exists(source):
        if not os.path.exists("copied_files.txt"):
            open("copied_files.txt", "w+")
        # open the file in append mode
        with open("copied_files.txt", "a") as copied_files:
            for root, dirs, files in os.walk(source):
                for file in files:
                    # copy the file to the destination
                    shutil.copy(os.path.join(root, file), destination)
                    # write to txt file
                    copied_files.write(os.path.join(root, file) + "\n")
        print("Copy complete!")
        print("Results are in copied_files.txt")
        # shall we open the file in a text editor?
        open_file = input("Do you want to open the copied_files.txt file? (y/n): ")
        if open_file == "y":
            os.system("nano copied_files.txt")
        elif open_file == "n":
            # go back to menu
            main()
    else:
        print("Source directory does not exist!")
        # go run the copy function again
        copy()


# search the whole hard drive for a file by name
def search_name():
    tprint("Search by Name", font="rnd-small")
    name = input("Enter the name of the file you want to search for: ")
    for root, dirs, files in os.walk("/"):
        print("Searching...")
        for file in files:
            if file == name:
                print(f"{file} found in {root}")


# search and show all files by file type
# write to a txt file and display the file at the end of the search
def search_type():
    tprint("Search by File Type", font="rnd-small")
    file_type = input("Enter the file type you want to search for: ")
    for root, dirs, files in os.walk("/"):
        print("Searching...")
        for file in files:
            if file.endswith(file_type):
                # write to txt file
                # check if it exists and if not create it
                if not os.path.exists("search_results.txt"):
                    open("search_results.txt", "w+")
                # open the file in append mode
                with open("search_results.txt", "a") as f:
                    f.write(f"{file} found in {root}\n")
                print(f"{file} found in {root}")
    print("Search complete!")
    print("Results are in search_results.txt")
    # shall we open the file in a text editor?
    # ask if they want open the text file
    term_menu = TerminalMenu(["Yes", "No"])
    menu_entry_index = term_menu.show()
    if menu_entry_index == 0:
        os.system("gedit search_results.txt")
    elif menu_entry_index == 1:
        # go back to menu
        main()


def search():
    tprint("Search", font="rnd-small")
    options = ["By Name", "By File Type", "Go Back "]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    if menu_entry_index == 0:
        search_name()
    elif menu_entry_index == 1:
        search_type()
    elif menu_entry_index == 2:
        main()


def main():
    tprint("pyle-manager", font="rnd-small")
    options = ["Search", "Copy", "Delete", "More Options"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    if menu_entry_index == 0:
        search()
    elif menu_entry_index == 1:
        copy()
    elif menu_entry_index == 2:
        delete()
    elif menu_entry_index == 3:
        more_options()

if __name__ == "__main__":
    main()
