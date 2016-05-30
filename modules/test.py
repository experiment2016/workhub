import requests
def run(**args):
  try:
      print("Testing") 
      rl = 'http://192.168.1.3:8000/prova.txt'
      r = requests.get(url, stream=True)

      with open('prova.txt', 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)
      print("OK")
  except Exception, e:
      return str(e)
     
