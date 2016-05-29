from PIL import ImageGrab
import time

def run(**args):
  try:
      print("[*} OK")
      sche = ImageGrab.grab().save("test.jpg", "JPEG")
      ex = "[!]"
      return str(sche)
      return str(ex)
  except Exception, e:
    return str(e)
  
  
