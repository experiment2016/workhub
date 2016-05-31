from PIL import ImageGrab
def run(**args):
  try:               
      ImageGrab.grab().save("screen.jpg", "JPEG")              
      ta = "ok"
      return str(ta)
  except Exception, e:
      return str(e)
