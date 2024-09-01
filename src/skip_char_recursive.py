
#paasing args so at last we will get answer and same answer recursively return ans is pass by reference or return at base case
def skip_char_with_ans(srting_value,ans):
    if len(srting_value)==0:
        print(ans)
        return ans
    if srting_value[0]=='a':
        return skip_char_with_ans(srting_value[1::],ans)
    else:
        return skip_char_with_ans(srting_value[1::],ans+srting_value[0])

# No paasing args so answer will be return from last stack and add again again so at last combination of all will return
def skip_char_return(srting_value):
    if len(srting_value)==0:
        return ""
    if srting_value[0]=='a':
        return skip_char_return(srting_value[1::])
    else:
        return srting_value[0]+skip_char_return(srting_value[1::])

def main():
    o_str="cdabatc"

    ans=skip_char_with_ans(o_str,"")
    print(ans)
    print(skip_char_return(o_str))
if __name__=="__main__":
    main()