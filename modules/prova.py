def run(*args, **kwargs):
    import os
    print("[*] Modulo attivo")
    files = os.listdir(".")
    return str(files)


