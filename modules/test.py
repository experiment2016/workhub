import requests
def run(**args):
  try:
      print("Testing") 
     # url='https://github.com/experiment2016/workhub/tree/master/data/post'
      url='https://192.168.1.2/post'
      files = {'upload_file': open('file.txt','rb')}
      r=requests.post(url,files=files)
  except Exception, e:
      return str(e)
     
