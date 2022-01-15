import os
from base64 import b64encode, b64decode

def write2file(filename, data):
    file = open(filename, "wb+")
    file.write(b64encode(data))
    file.close()
    del(file)
def readfromfile(filename):
    file = open(filename, 'rb')
    data = b64decode(file.read())
    file.close()
    del(file)
    return data
def checkContact(name):
    temp = os.getcwd()
    os.chdir("Contacts")
    for i in os.listdir():
        if i == name:
            print("This name is already in the registry.")
            os.chdir(temp)
            return 0
    os.chdir(temp)
    return 1
def makeContact(name):
    temp = os.getcwd()
    os.chdir("Contacts")
    os.mkdir(name)
    os.chdir(name)
    os.mkdir("Public Keys")
    os.mkdir("Private Keys")
    os.chdir(temp)