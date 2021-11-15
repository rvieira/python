#!/usr/bin/env python3

# generates password with letters, digits and special symbols
# Author: Ricardo Vieira
# Creation date: 18/01/2021
# Last change: 15/11/2021

import secrets
import string
import sys

default_pwd_len=20

def error():
    print("wrong parameter")
    
def pwd_len():
    if len(sys.argv) < 2:
        return(default_pwd_len)
    elif sys.argv[1].isdigit():
        return(sys.argv[1])
    else:
        error()
        return(default_pwd_len)
    # else password_length = first arg

def compliant_pwd(candidate_pwd):
    check_upper = check_lower = check_special_char = False
    
    for letter in candidate_pwd:
        if letter.isupper():
            check_upper = True
        if letter.islower():
            check_lower = True
        if letter in ('._+-'):
            check_special_char = True
    return check_lower and check_upper and check_special_char
        
password_length=int(pwd_len())
special_characters = '._+-'
password = ''
alphabet = string.ascii_letters + string.digits + special_characters
while not compliant_pwd(password):
    password = ''.join(secrets.choice(alphabet) for i in range(password_length))
print("Length:",password_length)
print("Password:",password)
