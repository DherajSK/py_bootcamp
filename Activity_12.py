def input_number():
    return list(map(int,input("Enter three numbers").split()))
def greatest(a):
    return a[0] if(a[0]>a[1])and(a[0]>a[2]) else a[1] if(a[1]>a[2])and(a[1]>a[0]) else a[2]	
    #return max(a[0],max(a[1],a[2]))
def display( a, res):
    print("{} is the greatest number among {},{},{}".format(res,a[0],a[1],a[2]))
def main():
    a = input_number()
    gret = greatest(a)
    display(a, gret)

if __name__ == "__main__":
    main()
