from PIL import ImageGrab
import time

def run(**args):
  try:
      print("[*} OK")
      sche = ImageGrab.grab().save("test.jpg", "JPEG")
      return str(sche)
  except Exception, e:
    return str(e)
  
  
