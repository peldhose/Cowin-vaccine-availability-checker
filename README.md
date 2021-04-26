# hospital-availability-checker
co win hosptal availability checker with pincode search n beeper - Hobby project.

I made this because, it became very hard for somebody to book for the slot on any hospital.i tried my best on pressing mobile screens for half a day for getting a slot,but slot comes n vanishes like flipkart deal.. so i decided to make a checker to automate checking process

## Requirements to  install 
```
  sudo apt-get install libasound2-dev python3.6-dev   build-essential libssl-dev libffi-dev
  pip3 install simpleaudio beepy
```

## Running H-checker;

```
  python3 checker.py <district number> <pincode to check> 
```

This will run checker in every 20s and checks API link for pincodes ( pincode+ 8 ),If found it alarms .


## District numbers
307 -- Ernakulam
301 -- Alapuzha
297 -- Idukki
299 -- Trivandrum  


Lets automate ;) 
Its jst a hobby project ... pls contibute if u feel it lacks some features.
#### Note: It works because district wise hospital Search API is open.


