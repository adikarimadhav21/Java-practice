
def password():
    pwrd="796115110113721110141108"
    rev_pwrd=pwrd[::-1]
    print(rev_pwrd)
    res=""


    i=0
    while(i<len(rev_pwrd)):
        x=rev_pwrd[i]+rev_pwrd[i+1]
        if int(x)==32:
            res=res+" "
        elif int(x) in range(65,91) or int(x) in range(97,100):
            res=res+chr(int(x))
        elif i+2<len(rev_pwrd) :
            x+=rev_pwrd[i+2]
            res=res+chr(int(x))
            i+=1


        i+=2
    print(res)

def min_group():
    input="PPPP@ppp@pp$pp"
    groups=input.split("@")
    min_l=float('inf') # large value
    for group in groups:
        subgroups=group.split("$")
        length=[len(subgroup) for subgroup in subgroups]
        min_l=min(min_l,min(length))
    print(min_l)

def string_comp():
    a="m2c2m4a8"
    m={}
    i=0
    while i<len(a):
        if a[i] in m:
            m[a[i]]=m[a[i]]+int(a[i+1])
        else:
            m[a[i]]= int(a[i+1])
        i+=2
    x= dict(sorted(m.items()))
    print(x)
password()
min_group()
string_comp()