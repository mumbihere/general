import random

unsorted_partitions = []
input_array = []

def quicksort(array):
    global input_array,unsorted_partitions
    input_array = array
    partition(0,len(input_array)-1)
    return input_array


'''partitions an input array and ensure the pivot has all numbers less than it to the left, and numbers greater to the right'''
def partition(start_index,end_index):

    global input_array, unsorted_partitions
    #randomly pick a pivot
    pivot_location = random.randint(start_index,end_index)
    #print('partitioning partition ' + str(start_index)+' upto '+str(end_index) +' pivot location '+str(pivot_location)+' input_array '+str(input_array)+' unsorted '+str(unsorted_partitions))

    pivot = input_array[pivot_location]
    pointer1 = start_index
    pointer2 = end_index 
    array_length = end_index + 1 #this should be the same as pointer2 less 1 initially

    
    while (pointer1 != pointer2 ):
        #scan the left partition (should be smaller than pivot)
        #lower_swap,upper_swap=0
        while  input_array[pointer1]<pivot :
            pointer1=pointer1+1
        else:
            lower_swap = input_array[pointer1]
            
        #scan the right partition(should be greater than pivot)
        while input_array[pointer2]>pivot :
            pointer2=pointer2-1
        else:
            upper_swap = input_array[pointer2]
            

        #swap
        input_array[pointer2] = lower_swap
        input_array[pointer1]= upper_swap      
       
        #print('post swap -  pointer1 '+str(pointer1)+' pointer2 '+str(pointer2) +' input array '+str(input_array) )

    #insert new unsorted partitions to unsorted list only of the partition has more than 1 element
    if pointer1-start_index >1:
        unsorted_partitions.append({'start':start_index,'end':pointer1})
        
    if (array_length-1) - pointer2 >1:
        unsorted_partitions.append({'start':pointer2+1,'end':array_length-1})

    #print(unsorted_partitions)
    #print(' pivot is now at position '+str(pointer1))
        
    while len(unsorted_partitions)>0:
        pat = unsorted_partitions.pop() #{'start':0,'end':5}
        partition_start = pat['start']
        partition_end = pat['end']
        partition(partition_start,partition_end)




print(quicksort([7, 8, 48, 78, 22,2,98,447,25,45,9,73]))




