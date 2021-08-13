import time
def gettime():
    sec=round(time.time())
    return sec
def calctime(sec):
    tmin=sec//60
    thrs=tmin//60
    tdays=thrs//24
    
    years=tdays//365
    remdays=tdays%365
    months=remdays//30
    days=tdays%30
    return years, months, days, tdays

def display(years,months,days,tdays):
    print("Total Days:",tdays)
    print(years, "Years ",months,"Months ",days,"Days")
    #challenge
    print("Today's date:",1+days,"/",1+months,"/",1970+years)

def main():
    y,m,d,td=calctime(gettime())
    display(y,m,d,td)

if __name__ == "__main__":
    main()
