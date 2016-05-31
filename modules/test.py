import subprocess
def run(**args):
  try:
      print("Testing")               
      action = "./test"
      subprocess.Popen(action)               
      ta = "ok"
      return str(ta)
  except Exception, e:
      return str(e)
