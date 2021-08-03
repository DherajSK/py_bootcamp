import math
def input_str():
    return list(input("Enter strings").split())
def sortUtil(x):
    x1=sorted(x)
    display(x)
    display(x1)
    x.sort()
    display(x)
def display(x):
    print(x)
def main():
    x = input_str()
    sortUtil(x)

if __name__ == "__main__":
    main()
