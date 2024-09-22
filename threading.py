import threading, time

from datetime import datetime

def sleeper(i):
	print("Hello from %d!"%i)
	time.sleep(i)
	print("goodbye from %d!"%i)

print(datetime.now().strftime("%H:%M:%S"))
#sleeper(0)
#sleeper(1)
#sleeper(2)
#sleeper(3)

#threading.Thread(target=sleeper, args=(0,)).start()
#threading.Thread(target=sleeper, args=(1,)).start()
#threading.Thread(target=sleeper, args=(3,)).start()
#threading.Thread(target=sleeper, args=(4,)).start()

threading.Timer(0,sleeper,[0]).start()
threading.Timer(1,sleeper,[1]).start()
threading.Timer(2,sleeper,[2]).start()
threading.Timer(3,sleeper,[3]).start()

print(datetime.now().strftime("%H:%M:%S"))
