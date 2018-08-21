#test module for trojan framework.  Retrieves the dir list on the remote poota, on which the trojan is excuting


import os

def run(**args):

    print ("[*] now running dirlister module")
    files = os.listdir(".")

    return str(files)