import requests
def run(**args):
  try:
      print("Testing") 
      goodie = "license.pdf"
     # url='https://github.com/experiment2016/workhub/tree/master/data/post'
      url='http://192.168.1.4:8000'
      upload_files = {'': open(goodie,'rb')}
      r=requests.post(url,files=upload_file)
  except Exception, e:
      return str(e)
