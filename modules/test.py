import os
def run(**args):
  try:
      print("[*} view")
      ex = os.system("type test.txt")
      return ex
  except Exception, e:
    return str(e)
  
  
