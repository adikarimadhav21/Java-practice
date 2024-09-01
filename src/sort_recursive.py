

def bubble(arr,r,c):
    if r==0:
        return
    if c<r:
        if arr[c]>arr[c+1]:
            arr[c],arr[c+1]=arr[c+1],arr[c]
        bubble(arr,r,c+1)
    else:
        bubble(arr,r-1,0)


def quick_sort(arr,high,low):

    if low>=high:
        return
    pivot=arr[low]
    start=low
    end=high
    while start<=end:
        while arr[start]<pivot:  # find left violation
            start+=1
        while arr[end]>pivot: # find right violation
            end-=1
        if start<=end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    quick_sort(arr,low,end)
    quick_sort(arr,start,high)



def main():
    a=[2,10,15,1,3]
   # bubble(a,len(a)-1,0)
    quick_sort(a,len(a)-1,0)
    print(a,end=" ")
if __name__=="__main__":
    main()