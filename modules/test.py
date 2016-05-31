import _winreg

def run(**args):
  try:
      exname = 'test.exe'
      pathex = 'C:\\Users\\test.exe'
      key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,'Software\Microsoft\Windows\CurrentVersion\Run',_winreg.KEY_SET_VALUE)
      _winreg.SetValueEx(key,exname,0,_winreg.REG_SZ,pathex) 
      key.Close()
      ta = "ok"
      return str(ta)
  except Exception, e:
      return str(e)

 



