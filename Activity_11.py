def input_number():
    return int(input("Enter a number"))
def add(a, b):
    return a+b;
def display( a, b, res):
    print("{}+{}={}".format(a,b,res))
def main():
    a = input_number()
    b = input_number()
    summation = add(a, b)
    display(a, b, summation)

if __name__ == "__main__":
    main()
