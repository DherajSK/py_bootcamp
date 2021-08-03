import math
def input_number():
    return int(input("Enter a number"))
def isPrime(a):
    fl=False
    if a>1:
        for i in range(2,math.sqrt(a)):
            if a%i==0:
                fl=True
                break
    return fl
def display(a,fl):
    if not fl:
        print("{} is Prime".format(a))
    else:
        print("{} is non-prime".format(a))
def main():
    a = input_number()
    flag = isPrime(a)
    display(a,flag)

if __name__ == "__main__":
    main()

