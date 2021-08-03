def input_number():
    return list(map(int,input("Enter three numbers").split()))
def greatest(a):
    return max(a[0],max(a[1],a[2]))
def display( a, res):
    print("{} is the greatest number among {},{},{}".format(res,a[0],a[1],a[2]))
def main():
    a = input_number()
    grt = greatest(a)
    display(a, grt)

if __name__ == "__main__":
    main()
