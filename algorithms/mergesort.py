'''
Function takes an unsorted array A and returns a sorted array.
It does this by recursively dividing array into smaller chunks until an array of size 1 is left. An array of size 1 is sorted by default.
Thereafter, work its way back up by recursively merging 2 sorted arrays into one sorted array
'''

def MergeSort (A):
    #1. Pick a mid point and that is used to divide the array into two. Midpoint is half the size of the array
    mid = int(len(A)/2)
    if mid>0:#Partition only if array has more than 1 element
        L = A[0:mid]
        R = A[mid:]
        #To recursively split the arrays into smaller arrays, have the function call itself
        MergeSort(L)
        MergeSort(R)
        Merger(L,R,A) #Recursively merge into one sorted array
    else:
        return

    return A


'''
This function merges/combines 2 sorted arrays into one array which is also sorted e.g. l=[1,2] and r = [0,7] into a=[0,1,2,7]
At any particular time the smallest of the 2 list is either the first/unpicked element of one of the arraylists.
Logic is to progressively overwrite the element in array A with the smallest of either list.
'''
def Merger(L,R,A):
    i,j,k = (0,0,0) # pointer variables for arrays l,r and a

    while i<len(L) and j<len(R): #while both arrays L and R have elements
        if L[i] <R[j]: #always insert the smaller element to sort from least to greatest
            A[k] = L[i]
            i=i+1
        else:   #when the 1st element in R is smaller, insert it instead.
            A[k] = R[j]
            j=j+1
        k = k+1
    else:
        while i<len(L): #while only L has elements i.e. R is exhausted
            A[k] = L[i]
            i=i+1
            k = k+1            
        while j<len(R): #Viceversa i.e. L is exhausted
            A[k] = R[j]
            j=j+1
            k = k+1
            
    return A

            

A=[2,6,12,5,9,17,0,4,8,3]
MergeSort(A)


