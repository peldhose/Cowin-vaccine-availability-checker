import requests
import time
import json
import winsound
import sys



#CONSTANTS
district = sys.argv[1]
Pincode =  int(sys.argv[2]) #683572  # 688006 'Fatima'
date = sys.argv[3]  # 'CHC'
Vname = sys.argv[4]
# Pincode=683572

# print (H_no)

SLEEP_TIME = 10

URL =  "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id="+district+"&date="+date+"&vaccine="+Vname
# print (URL )


def looper():
	# print ( " api call starts")
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
				print ("no hospitals found")
				print (resp['centers'])
				break

			for center in resp['centers']:
				 # print(center)
				# if HOSPITAL_NAME in center['name'] or BLOCK_NAME in center['block_name']:
				# if HOSPITAL_NAME in center['pincode']:#  or BLOCK_NAME in center['block_name']:
				# if ( center['pincode'] == Pincode )  :#  or BLOCK_NAME in center['block_name']:
				if ( center['pincode'] >= Pincode and center['pincode'] <= Pincode+8 )  :
					print(" found Hospital with Pincode  "+Pincode)
					print (center)
					call_alarm()
				else :
					print("No matching pincode found ")
					print (center)

def call_alarm():
	print('Alarm ... ')
	winsound.Beep(500, 250)
	looper()



looper()
