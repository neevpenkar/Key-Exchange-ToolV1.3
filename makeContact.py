import os

def makeContact(name):
    os.chdir("Contacts")
    os.mkdir(name)
    os.chdir(name)
    os.mkdir("Public Keys")
    os.mkdir("Private Keys")
print("This tool is for creating a new object:")
contactName = input("Please enter the name of the contact to be created: ")
makeContact(contactName)