import os
from diffiehellman import DiffieHellman
from base64 import b64encode, b64decode
from imps_funcs import *

p = 0
while not p:
    Cname = input("Please enter the name of the contact: ")
    p = checkContact(Cname)

makeContact(Cname)

key_obj = DiffieHellman(group=14, key_bits=540)
write2file("Contacts/" + Cname + "/Public Keys/half1.key", key_obj.get_public_key())
write2file("Contacts/" + Cname + "/Private Keys/privinitial.key", key_obj.get_private_key())

del(key_obj)
print("Done! Please send the PUBLIC half key to your contact")