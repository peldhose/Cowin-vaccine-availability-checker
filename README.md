# hospital-availability-checker
co win hosptal availability checker with pincode search n beeper - for personal purpose 

Requirements to  install 

sudo apt-get install libasound2-dev python3.6-dev   build-essential libssl-dev libffi-dev
pip3 install simpleaudio beepy

Running H-checker;

python3 checker.py <district number> <pincode to check> 

This will run checker in every 20s and checks API link for pincodes ( pincode+ 8 ),If found it alarms .

Lets automate ;) 
Its jst a hobby project ... pls contibute if u feel it lacks some features.
Note: It works because district wise hospital Search API is open.
