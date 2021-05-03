import requests
import time
import json
import beepy as beep
import sys



#CONSTANTS
district = sys.argv[1]
Pincode =  int(sys.argv[2]) #683572  # 688006 'Fatima'
date = sys.argv[3]  # 'CHC'
Vname = sys.argv[4]
# Pincode=683572

# print (H_no)

SLEEP_TIME = 20

URL =  "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id="+district+"&date="+date+"&vaccine="+Vname
print (URL )


def looper():
	# print ( " api call starts")
	# exit()
	# time.sleep(1)
	while True:
		time.sleep(SLEEP_TIME)
		resp = requests.get(URL)
		 # print("after reqst ")
        # print("*********************") 
		if resp.status_code != 200:
			print('ApiError {0}'.format(resp.status_code))
			time.sleep(SLEEP_TIME)
			pass
		else:
			resp = json.loads(resp.text)
			# resp.json
			if( len(resp['centers']) == 0 ):
				print ("no hospitals found")
				# print (resp['centers'])
				pass
			# print("------------------ /n ")
			for center in resp['centers']:
                # print(" ------------------ ")
				print(center['name'])
				# if HOSPITAL_NAME in center['name'] or BLOCK_NAME in center['block_name']:
				# if HOSPITAL_NAME in center['pincode']:#  or BLOCK_NAME in center['block_name']:
				# if ( center['pincode'] == Pincode )  :#  or BLOCK_NAME in center['block_name']:
				
				#pincode checker 
				# if ( center['pincode'] >= Pincode and center['pincode'] <= Pincode+8 )  :
				# 	print(" found Hospital with Pincode  ")
				# 	print (center)
				# 	# print (center['available_capacity'])
				# 	for session in center['sessions']:
				# 		# print (session['available_capacity'])
				# 		if(session['available_capacity'] != 0):
				# 			call_alarm()
				# 			print (session['available_capacity'])
				# 		else
				# 			print ("not aviallbe !!")
				# else :
				# 	print("No matching pincode found ")
				# 	# print (center)
								#aviablity checker
				for session in center['sessions']:
						print (session)
						if(session['available_capacity'] != 0):
							call_alarm()
							print (session['available_capacity'])
						else:
							print ("not aviallbe !!")


def call_alarm():
	print('Alarm ... ')
	beep.beep(4)
	return



looper()
