import lazylights
import time
import threading

def callback():
#To power off every bulbs connected to your router
	bulbs = lazylights.find_bulbs()
	lazylights.set_power(bulbs, False)
	
#To select only a 	
#	bulbs_by_name = {state.label.strip(" \x00"): state.bulb
#		for state in lazylights.get_state(bulbs)}
#	lazylights.set_power([bulbs_by_name['Nice']], False)
#	lazylights.set_power([bulbs_by_name['Right']], False)

timer = threading.Timer(60.0, callback) #this is a non-blocking time.sleep(60)
timer.start()  # after 60 seconds, 'callback' will be called


