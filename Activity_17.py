def convert(st):
    a=str()
    for tup in st:
        a+=tup[0]+"="+tup[1]+";"
    a=a.rstrip(';')
    return a
def display(x):
    print(x)
def main():
    x = [('system','s'),('database','d'),('username','u'),('password','p')]
    x1=convert(x)
    display(x1);
if __name__ == "__main__":
    main()
