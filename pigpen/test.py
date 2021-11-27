import json
import sys


def get_file(filename):
    with open(filename) as f:
        jsondict = json.loads(f.read())
    return jsondict

def get_name():
    if len(sys.argv) > 1:
        return(sys.argv[1])
    else:
        return('carina')

jsondict = get_file('/Users/ricardovieira/github/python/pigpen/jsondata.json')
name=get_name()
encrypted_name=''
for letter in name:
    encrypted_name+=jsondict[letter]
print(encrypted_name)
