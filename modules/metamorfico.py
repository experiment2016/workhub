
def run(**args):
  try:
      print("Testing")
      ta = "ok"
      return (ta).encode('utf-8')
  except Exception, e:
      return str(e)
