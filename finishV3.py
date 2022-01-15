import os
from diffiehellman import DiffieHellman
from base64 import b64encode, b64decode
from imps_funcs import *

cname = input("Please enter the name of the contact: ")
privdata = readfromfile("Contacts/" + cname + "/Private Keys/privinitial.key")

key_obj = DiffieHellman(group=14, key_bits=540)
key_obj.set_private_key(privdata)

pubdata = readfromfile("Contacts/" + cname + "/Public Keys/half2.key")
write2file("Contacts/" + cname + "/Private Keys/final.key", key_obj.generate_shared_key(pubdata))

