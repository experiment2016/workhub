import subprocess
import os

def run(**args):
  try:
     look = os.system("dir") 
     return str(look)
  except Exception, e:
      return str(e)
  
  
