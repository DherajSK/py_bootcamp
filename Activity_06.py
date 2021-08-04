x1 = list(map(int, input("Enter 5 values: ").split()))
x2=x1[:3]
x1[0]=x1[-1]=0
print("Sliced list",x2)
print("Replaced list 1",x1)
x2[0]=x2[-1]=0
print("Replaced list 2",x2)

#reverse
x1=x1[::-1]
print("Reversed list 1",x1)
