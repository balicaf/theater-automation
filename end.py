import lazylights
import time
import threading
#time.sleep(60)
def callback():
	bulbs = lazylights.find_bulbs()
#	bulbs_by_name = {state.label.strip(" \x00"): state.bulb
#		for state in lazylights.get_state(bulbs)}
#	lazylights.set_power([bulbs_by_name['Nice']], False)
#	lazylights.set_power([bulbs_by_name['Right']], False)
	lazylights.set_power(bulbs, False)

timer = threading.Timer(60.0, callback)
timer.start()  # after 60 seconds, 'callback' will be called


