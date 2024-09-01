"""
use same logic ,,subset process and unprocess
like dice have [1,2,3,4,5,6]
what is the combination to make target 4

""/4 the
1/3 2/2 3/1 4/0 ----
then
1/3 == 1,1/2,  1,2/1 1,3/0
2/2= 1,2/1, 2,2/0
same  other


"""

def dice(face,target,ans):
    result=[]
    if target==0:
        result.append(ans.copy())
        return result
    collect=[]
    for  i in range(1,face+1):
        if i>target:
            break
        ##ans.append(i)
       ## collect.extend(dice(face,target-i,ans))
        collect.extend(dice(face,target-i,ans+[i])) ##ans+[i] create new list each time
       ## ans.pop()
    return  collect



def main():
    print(dice(6,4,[]))

if __name__=="__main__":
    main()