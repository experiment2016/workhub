def run(**args):
    import os
    print("[*] Modulo attivo")
    files = os.listdir(".")
    return str(files)


