import requests
import time
import json
import beepy as beep
import sys



#CONSTANTS
H_number = sys.argv[1]
Pincode = 683572 #683572  # 688006 'Fatima'
# BLOCK_NAME = sys.argv[3]  # 'CHC'
# Pincode=683572

# print (H_no)

SLEEP_TIME = 10

URL =  "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id="+H_number+"&date=27-04-2021&vaccine=COVISHIELD"
# print (URL )


def looper():
	print ( " api call starts")
	# exit()
	# time.sleep(1)
	while True:
		time.sleep(SLEEP_TIME)
		resp = requests.get(URL)
		 # print("after reqst ")
		if resp.status_code != 200:
			print('ApiError {0}'.format(resp.status_code))
		else:
			resp = json.loads(resp.text)
			# resp.json
			if( len(resp['centers']) == 0 ):
				print ("no hostls")
				print (resp['centers'])
				looper()

			for center in resp['centers']:
				 # print(center)
				# if HOSPITAL_NAME in center['name'] or BLOCK_NAME in center['block_name']:
				# if HOSPITAL_NAME in center['pincode']:#  or BLOCK_NAME in center['block_name']:
				if ( center['pincode'] == Pincode )  :#  or BLOCK_NAME in center['block_name']:
					print(" found ")
					print (center)
					call_alarm()
				else :
					print("Not found ")
					print (center)
					looper()

def call_alarm():
	# import beepy
	print('Alarm ... ')
	beep.beep(4)
	# time.sleep(1)
	looper()
	# beep(sound=1)
	# sys.stdout.write("\a")
	# beep(3)



looper()
