def input_dict():
    n=int(input("Enter size of dict"))
    print("Enter dictionary")
    d=dict(input().split() for _ in range(n))
    return d
def sortUtil(d):
    res={k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    return res
def display(x,d):
    print("Original dictonary :",d)
    print("Sorted dictonary :",x)
def main():
    d=dict()
    d=input_dict()
    x=sortUtil(d)
    display(x,d);
if __name__ == "__main__":
    main()
