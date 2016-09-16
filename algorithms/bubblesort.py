
'''
The program goes through the elements of the array, everytime ensuring that the greatest unsorted element  finds its way to the end of the array.
In a way the large elements, bubble themselves to the top of the array. In a worst case scenario,in an array of n elements we'd need to bubble atleast n-1 elements since the last element would be sorted by default.
Two loops are used. The outermost loop keeping track of how many times the program makes a complete pass through the array and bubbles the largest unsorted element.
The inner loop goes through the individual elements comparing them and deciding if to swap. i is subtracted from n-1 in the second loop to ensure that this loop doesnt go through the entire array again but only the unsorted part.
If the program has gone through the array i times, then it means that the greatest i elements have already been bubbled to the last i positions.
Essentially we use how many times we have gone through the array to determine the indices of the unsorted elements, in this case 0 to (n-1)-i
'''

def bubblesort(A):
    i=0
    n=len(A)
    while i<n-1:
        j,swaps = (0,0)
        while j<(n-1)-i:  
            temp = 0
            if A[j]>A[j+1]:
                #Swap
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                swaps = swaps+1
            j=j+1
        if swaps ==0:#If there is not a single swap the entire pass, then the array is already sorted and no need to continue
            print(' Array is now sorted ')
            return             
        i=i+1
    return A
            
A=[2,6,12,5,9,17,0,4,8,3]
bubblesort(A)

Hallo
