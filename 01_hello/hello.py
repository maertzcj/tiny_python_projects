#!/usr/bin/env python3
# Say hello

print('Hello, World!')


###################################################
###__________________NOTES__________________#######
###################################################

###shebang - Use the environment program to find python3

###Command Line Notes
# cd tiny_python_projects/01_Hello
# echo $PATH = see list of directories where the OS is looking to find python3 program
# env = put me directly into the repl environment; exit() to leave
# ls = show listing
# pip install ~programname~
# mak test = pymake test

###Test.py file
# To Run the MakeFile/ test the code, use 'pymake test' to run
# The third test in test.py does not run on windows. On windows only .exe, .bat, and .cmd files can be executable. There is no such thing as an executable .py file on Windows. Changed test to be same as test 2 to get around this

###Ch 1 Pt 5 (understanding $PATH)
# How to make a bin in Home directory - This allows you to run a program from anywhere on your machine
# Step 1: mkdir ~/bin
# Step 2: Copy hello.py over to the $HOME dir
# Step 3: Check if hello.py is in the home dir (~/bin) by using 'which'
# Step 4: use 'ls ~/bin' to see what is in the dir
#Q - How to update a file in ~/bin???

###Ch 1 Pt 6 (adding an argument)
#
#
#

