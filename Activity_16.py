def input_str():
    return input("Enter string")
def convert(st):
    res=list()
    for token in st.split(';'):
        item=token.split('=')
        res.append(tuple(item))
    return res
def display(x):
    print(x)
def main():
    x = input_str()
    x1=convert(x)
    display(x1);
if __name__ == "__main__":
    main()
