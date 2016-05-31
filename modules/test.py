import requests

def run(**args):
  try:
     print("[*] reading")
   
     goodie = "file.txt"
     url = 'https://raw.githubusercontent.com/experiment2016/workhub/master/file.txt'
     r = requests.get(url, stream=True)

     with open(goodie, 'wb') as fd:
         for chunk in r.iter_content(chunk_size=1024):
             fd.write(chunk)
     fd.close()
     te = "ok"
     return str(te)
     
  except Exception, e:
      return str(e)
