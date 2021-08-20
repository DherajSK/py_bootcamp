from itertools import combinations_with_replacement
from itertools import permutations

def getcombinationsutil(num,threeorfour):
    comb1=list()
    for iter1 in range(1,num+1):
        if(threeorfour):
            comb=list(combinations_with_replacement([1, 2, 3], iter1))
        else:
            comb=list(combinations_with_replacement([1, 2, 3, 4], iter1))
        for iter2 in comb:
            if(sum(iter2)==num):
                comb1.append(iter2)
##    print(a)
##    print("---------------------")
    perm1=list()
    for i in comb1:
        perm = permutations(i)
        perm1.append(list(set(perm)))
    #print(perm1)
    return perm1

def getcombinations(freq,keypad,num):
    if(num==7 or num==9):
        permut=getcombinationsutil(freq,False)
    else:
        permut=getcombinationsutil(freq,True)

    keypad=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    combin=list()
    for x in permut:
        for y in x:
            temp=""
            for z in y:
                temp=temp+(keypad[num][z-1])

            combin.append(temp)
    return combin
def getnum():
    return input("Enter numbers")

def preprocess(st):
    s=""
    for i in range(1,len(st)):
        if st[i-1]!=st[i]:
           s=s+st[i-1]+"$"
        else:
            s=s+st[i-1]
    s=s+st[-1]+"$"
    return s
def strperm(num,keypad,ans,st,i):
    while(True):
        idx=num.find("$",i+1)
        if(idx-i==2):
            st=st+(keypad[int(num[idx-1])][0])
        else:
            if(idx==-1):
                break
            combination=getcombinations(idx-i-1,keypad,int(num[idx-1]))
            #print(combination)
            for substring in combination:
                strperm(num,keypad,ans,st+substring,idx)
            return
        i=idx
        if(i==-1):
            break
##            return
    ans.append(st)
    return ans
   
def main():
    prest=preprocess(getnum())
    #print(prest)
    keypad=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    ans=list()
    strperm(prest,keypad,ans,"",-1)
    print(ans)
main()
