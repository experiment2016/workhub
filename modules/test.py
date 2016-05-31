import subprocess
def run(**args):
  try:               
      action = "test.exe"

      subprocess.Popen(action)               
      ta = "ok"
      return str(ta)
  except Exception, e:
      return str(e)
     


