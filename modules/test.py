import requests

def run(**args):
  try:
     print("[*] reading")
   
     goodie = "nonexist.txt"
     url = 'http://192.168.1.4:8000/nonexist.txt'
     r = requests.get(url, stream=True)

     with open(goodie, 'wb') as fd:
         for chunk in r.iter_content(chunk_size=1024):
             fd.write(chunk)
     fd.close()
     te = "ok"
     return str(te)
     
  except Exception, e:
      return str(e)
