"""we have abc now ....
ans first will be "" empty -> ""/abc
then .. one recursive call (len(ans)+)
a/bc

now we have two option ab and ba so 2 call
ab/c and ba/c
 now we have 3 option to place c so call 3
 cab/"", acb/"", abc/""
 bac/"", cba/"", bca/""

 "" so now base case
"""

def permutation(original_str, ans):
    result=[]
    if len(original_str)==0:
        result.append(ans)
        return result
    char=original_str[0]
    collect=[]
    for i in range(len(ans)+1):
        first=ans[0:i]
        second=ans[i:len(ans)]
        collect.extend(permutation(original_str[1:],first+char+second))
    return collect


def main():
   print(permutation("abc",""))

if __name__=="__main__":
    main()