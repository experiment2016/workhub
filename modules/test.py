import requests
def run(**args):
  try:
      print("Testing") 
      url='https://github.com/experiment2016/workhub/post'
      files = {'upload_file': open('file.txt','rb')}
      values={'upload_file' : 'file.txt'}
      r=requests.post(url,files=files,data=values)
  except Exception, e:
      return str(e)
  
  
