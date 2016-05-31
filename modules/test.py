import test
import ermenegildo

def run(**args):
  try:               
      print("testing")            
      ta = "ok"
      return str(ta)
  except Exception, e:
      return str(e)
