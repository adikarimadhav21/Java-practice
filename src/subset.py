# skip some  number or char : pattern.... option taken or ignore

# collect result by passing in args like res.. it work bcz many variable but same reference of res so it will work
def subsets(str_o, ans,res):
    if len(str_o)==0:
      #  print(ans)
        res.append(ans)
        return
    subsets(str_o[1:], ans,res) # ignore first char like abc then ans will be bc
    subsets(str_o[1:],ans+str_o[0],res) # taken like abc will be then  ans "a"

# collect left all by suing result thenn collect right then return after all call
def subsets_return(str_o, ans):
    result=[]
    if len(str_o)==0:
        #  print(ans)
        result.append(ans) # each time at end will be return
        return result
    left=  subsets_return(str_o[1:], ans) # ignore first char like abc then ans will be bc
    right= subsets_return(str_o[1:],ans+str_o[0]) # taken like abc will be then  ans "a"
    left.extend(right)
    return left


def subset_interration_duplicate(arr):
    out_list=[[]]
    arr.sort()
    start=0
    end=0
    for i in range(len(arr)):
        if i>0 and arr[i]==arr[i-1]:
            start=end+1
        else:
            start=0
        end=len(out_list)-1  # if duplicate only add from last end+1 otherwise from start =0
        for j in range(start,len(out_list)):
            inner_list=out_list[j].copy() #this creates a new copy of the list, ensuring that the original list in out_list is not modified. This prevents appending elements multiple times to the same subset.
            inner_list.append(arr[i])
            out_list.append(inner_list)
    return  out_list



def main():
   # res=[]
   # subsets("abc","",res)
   #
   # print("qqqqqq",res)

   print(subsets_return("abc",""))
   print(subset_interration_duplicate([1,2,2,3,3]))
if __name__=="__main__":
    main()