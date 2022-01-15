from diffiehellman import DiffieHellman
from base64 import b64encode, b64decode
from imps_funcs import *

filename = input("Please enter the name of the file received from contact: ")
data = readfromfile(filename + ".key")

key_obj = DiffieHellman(group=14, key_bits=540)

p = 0
while not p:
    cname = input("Please enter the name of the contact: ")
    p = checkContact(cname)
makeContact(cname)

write2file("Contacts/" + cname + "/Public Keys/half1.key", data)
write2file("Contacts/" + cname + "/Public Keys/half2.key", key_obj.get_public_key())
write2file("Contacts/" + cname + "/Private Keys/final.key", key_obj.generate_shared_key(data))

print("Done! Your Key is established! Now send your PUBLIC half key back")