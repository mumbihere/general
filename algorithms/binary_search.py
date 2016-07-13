'''
Binary Search algorithm assumes a sorted array A and a search element x. The goal is to find if the element x exists in A.
It does this in an almost similar fashion as the quicksort algorithm, it recursively breaks down the halves and compares element x with the mid.
It does this so that it can figure out whether to discard the left or the right side of the array.
'''

array  = []
searched_number = None

def BinarySearch(A,x):
    global searched_number
    global array 
    searched_number = x
    array = A
    start = 0
    end = len(A)
    search_result = search(start, end)
    if search_result ==None:
        print( 'Element '+ str(x)+' does not exist in the array')
    else:
        print('Element '+ str(x)+' exists at location ' +str(search_result))



def search(start,end):
    while start!=end:
        mid = int((start+end)/2)
        if searched_number == array[mid]:
            return mid
        elif searched_number < array[mid]:
            #Discard the right side of the array
            end = mid
            search(start,end)
        elif searched_number > array[mid]:
            #Discard the left side of the array
            start = mid+1
            search(start,end)
    else:
        return None

Z=[0, 2, 3, 4, 5, 6, 8,9, 12, 17]
w=9
x=81
BinarySearch(Z,w)
BinarySearch(Z,x)      
