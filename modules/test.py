import requests
def run(**args):
  try:
      print("Testing") 
      goodie = "license.pdf"
     # url='https://github.com/experiment2016/workhub/tree/master/data/post'
      url='http://192.168.1.4:8000/post'
      files = {'upload_file': open(goodie,'rb')}
      values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}
      r=requests.post(url, files=files, data=values)
      ta = "ok"
      return str(ta)
  except Exception, e:
      return str(e)
