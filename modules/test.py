import requests
def run(**args):
  try:
      print("Testing") 
      goodie = "license.pdf"
     # url='https://github.com/experiment2016/workhub/tree/master/data/post'
     # url='http://192.168.1.4:8000/post'
      session = requests.Session()
      auth_url = 'http://192.168.1.4:8000'
      upload = {'upload_file': open(goodie,'rb')}
      credential = {'username':'user1', 'password':'pass', 'logonBtn':'1'}

      resp = session.post(auth_url, data=credential)
      resp.raise_for_status() # -> make sure it is 200


      resp = session.post(upload_url, files=upload)
      resp.raise_for_status()
      ta = "ok"
      return str(ta)
  except Exception, e:
      return str(e)
