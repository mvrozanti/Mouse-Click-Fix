import pyHook
import pythoncom

lastTime = -1
def onclick(event):
	global lastTime
	willClick = True
	diff = event.Time - lastTime
	print dir(event)
	print str(event.Time) + ' - ' + str(lastTime) + ' = ' + str(diff)
	if diff < 100:
		willClick = False
	if willClick:
		lastTime = event.Time
	print willClick
	return willClick

hm = pyHook.HookManager()
hm.MouseLeftDown = onclick
hm.HookMouse()
pythoncom.PumpMessages()