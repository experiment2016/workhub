import os

def run(**args):
    print("[*] Modulo attivo")
    files = os.listdir(".")
    return str(files)


