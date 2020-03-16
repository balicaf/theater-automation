import lazylights
import time

#to power on every bulbs connected to your router
bulbs = lazylights.find_bulbs(expected_bulbs=3, timeout=5)
lazylights.set_power(bulbs, True)

#If you want to light on only a few of your bulbs:
#bulbs_by_name = {state.label.strip(" \x00"): state.bulb
#		for state in lazylights.get_state(bulbs)}
#print (bulbs_by_name)
#lazylights.set_power([bulbs_by_name['Nice']], True)
#lazylights.set_power([bulbs_by_name['Right']], True)

