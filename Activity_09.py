import math
l,b,h=map(float,input("Enter l,b,h").split())
k=(l**2)+(b**2)+(h**2)
vol=(b**2)*(h**2)/math.sqrt(k)
vol=round(vol,3)
print("Volume of tromboloid",vol);
rad=((3*vol)/(4*math.pi))**(1./3.)
rad=round(rad,3)
print("Radius of sphere with above given vol",rad);
