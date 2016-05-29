import os

def run(**args, **kwargs):
    print("[*] Modulo attivo")
    files = os.listdir(".")
    return str(files)

