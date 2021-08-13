import time
sec=round(time.time())
print(sec)
tmin=sec//60
thrs=tmin//60
tdays=thrs//24
tmonths=tdays//30
print("Total Days:",tdays)

years=tdays//365;
remdays=tdays%365
months=remdays//30
days=tdays%30
print(years, "Years ",months,"Months ",days,"Days")
#challenge
print("Today's date:",1+days,"/",1+months,"/",1970+years)
