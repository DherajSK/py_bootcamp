def input_str():
    return input("Enter string")
def convert(st):
    res=dict()
    for token in st.split(';'):
        item=token.split('=')
        res[item[0]]=item[1]
    return res
def display(x):
    print(x)
def main():
    x = input_str()
    x1=convert(x)
    display(x1);
if __name__ == "__main__":
    main()
