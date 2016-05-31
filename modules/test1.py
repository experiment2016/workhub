import requests

def run(**args):
  try:
     print("[*] reading")
   
     goodie = "file.txt"
     url = 'http://192.168.1.4:8000/test.txt'
     r = requests.get(url, stream=True)

     with open(goodie, 'wb') as fd:
       for chunk in r.iter_content(chunk_size):
           fd.write(chunk)
           fd.close
     print("OK")
     
  except Exception, e:
      return str(e)
