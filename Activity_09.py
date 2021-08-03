import math
l,b,h=map(float,input("Enter l,b,h").split())
k=(l**2)+(b**2)+(h**2)
vol=(b**2)*(h**2)/math.sqrt(k)
print("Volume of tromboloid %.3f"% vol)
rad=((3*vol)/(4*math.pi))**(1./3.)
print("Radius of sphere with above given vol %.3f"% rad)
