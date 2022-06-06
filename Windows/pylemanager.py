#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
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

# dpendencies:
import shutil
import time
import os
import glob
import sys

# define function  for command listing
def list_commands():
    print("")
    print("Commands:")
    print("  listdir")
    print("  search")
    print("  copy")
    print("  shred")
    print("  info")
    print("  exit")
    print("  menu")
    print("  help")
    print("")

# display license
def licencse():
    print("PyleManager v" + version)
    print("Copyright (c) 2022 Jeremy Stevens")
    print("")
    print("This program is free software: you can redistribute it and/or modify")
    print("it under the terms of the GNU General Public License as published by")
    print("the Free Software Foundation, either version 3 of the License, or")
    print("(at your option) any later version.")
    print("")
    print("This program is distributed in the hope that it will be useful,")
    print("but WITHOUT ANY WARRANTY; without even the implied warranty of")
    print("MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the")
    print("GNU General Public License for more details.")
    print("")
    print("You should have received a copy of the GNU General Public License")
    print("along with this program.  If not, see <http://www.gnu.org/licenses/>.")

# def serac
def search():
    print("")
    print("Search:")
    print("  search <name>")
    print("  search <type>")
    print("")

# def copy
def copy():
    print("")
    print("Copy:")
    print("  copy <source> <destination>")
    print("")

def list_dir():
    print("")
    print("List Directory:")
    print("  listdir")
    print("")

def shred():
    print("")
    print("Shred:")
    print("  shred <file>")
    print("")

def info():
    print("")
    print("Info:")
    print("  info <file>")
    print("")

# main entry point
def main():
    # display license
    licencse()
    list_commands()
    userinput = input("Enter command: ")
    if userinput == "listdir":
        list_dir()
    elif userinput == "search":
        search()
    elif userinput == "copy":
        copy()
    elif userinput == "shred":
        shred()
    elif userinput == "info":
        info()
    elif userinput == "exit":
        exit()
    elif userinput == "menu":
        list_commands()
    elif userinput == "help":
        help()

if __name__ == "__main__":
    main()