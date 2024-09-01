
def min_glasses(glasses,target):
    no_glasses = 1
    for g in glasses[::-1]:
         if target <=g:
             return no_glasses
         else:
             no_glasses+=1
             target = target - g
    return 0

min_glasses([1,3,5,7,10],6)