def search(start,end,search_text):
    comparisons = 0
    while start!=end:
        mid = int((start+end)/2)
        if search_text == common_pwds[mid]:
            comparisons += 1 
            return True,comparisons
        elif search_text < common_pwds[mid]:
            #Ignore the right side of the array
            end = mid
            comparisons += 1 
            search(start,end,search_text)
        elif search_text > common_pwds[mid]:
            #Ignore the left side of the array
            start = mid+1
            comparisons += 1 
            search(start,end,search_text)
    else:
        return False,comparisons


test_array = ['apple','bg0od','bye','duties','Friday']
truesearch = search(0,len(test_array),'apple')
falsesearch = search(0,len(test_array),'zucchini')

print(truesearch)
print(falsesearch)

