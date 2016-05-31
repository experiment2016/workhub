import requests
def run(**args):
  try:
      print("Testing") 
      goodie = "guide.pdf"
      url='https://github.com/experiment2016/workhub/tree/master/data'
      auth=('experiment2016','test101')
      files = {'file': open(goodie,'rb')}
      r=requests.post(url,auth,files=files)
      ta = "ok"
      return str(ok)
  except Exception, e:
      return str(e)
