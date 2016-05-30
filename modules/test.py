import os

def run(**args):
  try:
     look = os.system("notepad") 
     return str(look)
  except Exception, e:
      return str(e)
  
  
