import os

def run(**args):
  print("[*] vedendo il file")
  file = os.uname()
  return str(file)

run()

