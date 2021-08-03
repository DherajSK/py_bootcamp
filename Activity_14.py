import math
def input_number():
    l,b,h=map(float,input("Enter l,b,h").split())
    return l,b,h
def calcVol(l,b,h):
    k=(l**2)+(b**2)+(h**2)
    vol=(b**2)*(h**2)/math.sqrt(k)
    rad=((3*vol)/(4*math.pi))**(1./3.)
    return vol,rad
def display( vol, rad):
    print("Volume of tromboloid %.3f" %vol)
    print("Radius of sphere with above given vol %.3f" %rad)
def main():
    l,b,h = input_number()
    vol,rad = calcVol(l,b,h)
    display(vol,rad)

if __name__ == "__main__":
    main()
