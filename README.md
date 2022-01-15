# Key-Exchange-ToolV1.3
This tool will help you perform Diffie Hellman key exchanges with your contacts via email. Version 1.3 will take in .key files provided by the user and save .key files to the respective contact's directory. Following versions will implement encryption as well, and more features will be added. As of version 1.3, the code is lesser than bare minimum.
As I had trouble creating the .exe files, the user needs to have the key exchange library installed: https://pypi.org/project/py-diffie-hellman/ (instructions for installation included.) 

The first step will be to run the setup file. It shall create a "Contacts" folder. 

1. To start a key exchange with a contact, run the "senderV3.py" file in a Python 3 environment. Enter a contact name which is unique (as it is stored in a respectively-named folder), and as you may see while exploring the directory system, this will create two folders to store the public and private parts of keys; the final derived key being stored in the "Private Keys" folder. In the future, mostly after a bare-minimum GUI will be introduced, an extra layer of encryption may be added to these keys as it is important for these to be encrypted (the access to these keys will likely be via asymmetric encryption coupled with a password or only the password).
2.  
