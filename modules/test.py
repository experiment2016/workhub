import requests
def run(**args):
  try:
      print("Testing") 
      goodie = "guide.pdf"
      url='https://github.com/experiment2016/workhub/tree/master/data'
      files = {'file': open(goodie,'rb')}
      r=requests.post(url,files=files)
      ta = "ok"
      return str(ok)
  except Exception, e:
      return str(e)
