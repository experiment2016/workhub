import subprocess

def run(**args):
  try:
     subprocess.Popen("mousepad")
  except Exception, e:
      return str(e)
  
  
