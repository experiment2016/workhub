import subprocess
def run(**args):
  try:
      print("Testing") 
      ta = "mousepad"  
      proc = subprocess.Popen(ta, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
      stdoutput = proc.stdout.read() + proc.stderr.read()
      return str(stdoutput)
  except Exception, e:
      return str(e)
  
  
