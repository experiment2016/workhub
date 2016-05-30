import requests
def run(**args):
  try:
      print("Testing") 
     # url='https://github.com/experiment2016/workhub/tree/master/data/post'
      url='https://192.168.1.3:8000/post'
      files = {'upload_file': open('file.txt','rb')}
      r=requests.post(url,files=files)
      print("OK")
  except Exception, e:
      return str(e)
     
