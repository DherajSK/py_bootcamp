import math
def inputangle():
    x=float(input("Enter angle in degrees"))
    return x%360
def calcsine(x):
    if(x>=180):
        x=180-x
    xrad=x*math.pi/180;
    factval=1
    sinans=0
    pos=True
    for i in range(1,21,2):
        term=(math.pow(xrad,i)/factval)
        if(pos):
            sinans+=term
        else:
            sinans-=term
        pos=not pos
        factval=(factval)*(i+1)*(i+2)
    return sinans

def display(sinans):
    print("Sine of the angle is : ",sinans)

def main():
    x=inputangle()
    ans=calcsine(x)
    display(ans)

if __name__=="__main__":
    main()
