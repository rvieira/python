#!/usr/bin/env python3

# generates password with uppercase and lowercase letters, digits and special symbols
# Author: Ricardo Vieira
# Creation date: 18/01/2021
# Last change: 18/11/2021

import secrets
import string
import sys
import configparser

config = configparser.ConfigParser()
config.read('pwd.ini')
default_pwd_len = config.getint('defaults','pwd_length')
min_pwd_length=4
errors = ["No errors","Usage: pwd.py [password length]","Password length too short"]

def error(err_code):
    print(errors[err_code])
    exit(err_code)
    
def pwd_len():
    if len(sys.argv) < 2:
        return(default_pwd_len)
    elif sys.argv[1].isdigit():
        if int(sys.argv[1]) >= min_pwd_length:
            return(sys.argv[1])
        else:
            error(2)
    else:
        error(1)
        return(default_pwd_len)

def compliant_pwd(candidate_pwd):
    check_upper = check_lower = check_special_char = check_digit = False
    
    for letter in candidate_pwd:
        if letter.isupper():
            check_upper = True
        if letter.islower():
            check_lower = True
        if letter.isdigit():
            check_digit = True
        if letter in ('._+-'):
            check_special_char = True
    return check_lower and check_upper and check_special_char and check_digit
        
password_length=int(pwd_len())
special_characters = '._+-'
password=''
alphabet = string.ascii_letters + string.digits + special_characters
while not compliant_pwd(password):
    password = ''.join(secrets.choice(alphabet) for i in range(password_length))
print("Length:",password_length)
print("Password:",password)
