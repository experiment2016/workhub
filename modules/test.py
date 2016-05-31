import requests
def run(**args):
  try:
      print("Testing") 
      goodie = "guide.pdf"
      url='https://github.com/experiment2016/workhub/tree/master/data/'
    #  url='http://192.168.1.4:8000'
      files = {'upload_file': open(goodie,'rb')}
      r=requests.post(url,files=files)
      ta = "ok"
      return str(ta)
  except Exception, e:
      return str(e)
