import requests
def run(**args):
  try:
      print("Testing") 
      url='https://github.com/experiment2016/workhub/tree/master/data/'
      files = {'upload_file': open('file.txt','rb')}
      r=requests.post(url,files=files)
  except Exception, e:
      return str(e)
     
