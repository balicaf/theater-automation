import lazylights
import time
bulbs = lazylights.find_bulbs(expected_bulbs=3, timeout=5)
#bulbs_by_name = {state.label.strip(" \x00"): state.bulb
#		for state in lazylights.get_state(bulbs)}
#print (bulbs_by_name)
#lazylights.set_power([bulbs_by_name['Nice']], True)
#lazylights.set_power([bulbs_by_name['Right']], True)
lazylights.set_power(bulbs, True)
