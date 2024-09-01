def swap(a,b):
    a,b=b,a
    return
def bubble_sort(input):
    for i in range(len(input)):
        for j in range(len(input)-1-i):
            if input[j]>input[j+1]:
              temp=input[j]
              input[j]=input[j+1]
              input[j+1]=temp
def selection_sort(input):
     for i in range(len(input)):
         min=input[i]
         for j in range(i+1,len(input)):
             if min >input[j]:
                 min=input[j]
                 input[j]=input[i]
                 input[i]=min
                 

def insertion_sort(input):
    
    for i in range(1,len(input)):
        current=input[i]
        for j in range(i+1):
            pass

def binary_search(input,target):
    pass

def quick_sort(input):
    pass

def merge_sort(input):
    if len(input)<=1:
        return input
    mid=len(input)//2
    left=merge_sort(input[:mid])
    right=merge_sort(input[mid:])
    return merge(left,right)

def merge(left,right):
    i=j=0
    result=[]
    while i< len(left) and  j< len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])  
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])   
    return result       
def heap_sort(input):
    pass

def main ():
    a=[10,20,1,45,20,100]
   # bubble_sort(a)
   # selection_sort(a)
    b= merge_sort(a)
    for num in b:
        print(num, end=" ")
if __name__=='__main__':
    main()

# def quick_sort(arr):
#     # Base case: if the array is of length 0 or 1, return it
#     if len(arr) <= 1:
#         return arr
    
#     # Choose the first element as the pivot
#     pivot = arr[0]
    
#     # Partition the array into three parts: 
#     # 1. elements less than pivot
#     # 2. elements equal to pivot
#     # 3. elements greater than pivot
#     less = [x for x in arr[1:] if x < pivot]
#     equal = [x for x in arr if x == pivot]
#     greater = [x for x in arr[1:] if x > pivot]
    
#     # Recursively sort the less and greater parts, then combine
#     return quick_sort(less) + equal + quick_sort(greater)

# # Example usage
# arr = [10, 7, 8, 9, 1, 5]
# sorted_arr = quick_sort(arr)
# print("Sorted array:", sorted_arr)
