import os
def run(**args):
  try:
      print("[*} view")
      ex = os.system("type test.txt")
      return str(ex)
  except Exception, e:
    return str(e)
  
  
