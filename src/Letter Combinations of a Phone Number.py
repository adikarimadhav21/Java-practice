"""
solve like subset.. ignore and taken
input="12"
then
""/"12" then a/2  b/2 c/2


"""

k_v={
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz"
}
def letterCombination(digits:str,ans):
    result=[]
    if len(digits)==0:
        result.append(ans)
        return result
    value=k_v[digits[0]]
    collect=[]
    for char in value:
        collect.extend( letterCombination(digits[1:],ans+char))
    return  collect

def letterCombinationWithIndex(digits:str,ans):
    result=[]
    if len(digits)==0:
        result.append(ans)
        return result
    value=int(digits[0])
    collect=[]
    for i in range((value-1)*3,value*3):
        char= ord('a')+i
        collect.extend( letterCombinationWithIndex(digits[1:],ans+chr(char)))
    return  collect

def letterCombinationCount(digits:str,ans):
    if len(digits)==0:
        return 1
    value=k_v[digits[0]]
    count:int=0
    for char in value:
        count=count+ letterCombinationCount(digits[1:],ans+char)
    return  count


def main():
    print(letterCombination("23",""))
    print(letterCombinationCount("23",""))
    print(letterCombinationWithIndex("12",""))

if __name__=="__main__":
    main()