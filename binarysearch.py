#Binary search is an algorithm in which we search for an element in a sorted array
#The search for the element takes place by continuously halving the array
#This process continues until we have found the target element
#Binary search is preferred over linear search due to reduced time complexity

def binary_search(element,list):
    start=0
    end=len(list)
    middle=0
    steps=0

    while start<=end:
        print("step ",steps,":",str(list[start:end+1]))
        middle=(start+end)/2
        steps=steps+1
        if element==list[middle]:
            return middle
        if element<list[middle]:
            end=middle-1
        if element>list[middle]:
            start=middle+1  
    return -1

mylist=[1,2,3,4,5]
target=4
binary_search(target,mylist)



        
        