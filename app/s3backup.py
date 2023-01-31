import sys
import re
import json
from colorama import Fore, Back, Style

def phoneIsValid(phone):
    result = re.search('^\d{2}9\d{8}$', phone)
    return result

def loadPhoneList():
    fileP = open('private/phones.json', 'r')
    listP = fileP.read()
    phones = json.loads(listP)
    
    return phones

def savePhoneList(phoneList):
    obJson = json.dumps(phoneList)
    fileP = open('private/phones.json', 'w')
    fileP.write(obJson)
    fileP.close()

def addPhone():
    phone = input('Enter the phone number: ')
    if(phoneIsValid(phone) is None):
        print(Fore.RED + "Invalid phone number")
    else:
        phones = loadPhoneList()
        if(phones.count(phone)):
            print(Fore.RED + "The phone already exists in the list")
        else:
            phones.append(phone)
            savePhoneList(phones)
            print(Fore.GREEN + "The list was been updated")

def listPhones():

    phones = loadPhoneList()
    
    listSize = len(phones)

    for x in range(listSize):
        print("Item:", x, " | Phone:", phones[x])

def removePhone():
    index = int(input("Enter the phone index: "))
    phones = loadPhoneList()
    listSize = len(phones)

    if(listSize == 0):
        print(Fore.RED + 'The phone list is empty')
        return 0
    
    if(index == 0 or index < listSize):
        phones.pop(index)
        savePhoneList(phones)
        print(Fore.GREEN + "The list was been updated")
    else:
        print(Fore.RED + 'The index ', index, ' not exists')

commands= {
    'remove': removePhone, 
    'list': listPhones,
    'add': addPhone
}

if(len(sys.argv) < 2):
    print(Fore.RED + 'Did you mean add, list or remove?')

else:

    command = sys.argv[1]
    if(commands.get(command) is None):
        print(Fore.RED + "Command", command, 'does not exist')
    else:
        commands[command]()