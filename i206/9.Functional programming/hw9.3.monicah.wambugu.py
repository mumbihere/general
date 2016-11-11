#Homewoek 9: Part 3
#references: https://www.youtube.com/watch?v=WOCV2UcxNrI

from operator import itemgetter

data={};cumulative_data = {};path = {};elements=[];


#Output the path
def path_of_element(e,row):
    if row >= 0:
        column = cumulative_data[row].index(e)
        elements.append(data[row][column])
        new_element = path[row][column][1]
        row =row-1
        #print(new_element)
        path_of_element(new_element, row)

def main():
    while(True):
        print("Enter the file name to read:")
        filename = input('> ')
        try:
            #1.Read file
            with open(filename, 'r') as f:
                rows = (row for row in f if len(row.split())>0) 
                for row_num, row in enumerate(rows, 0):
                    data[row_num] = list(map(int, row.split()))
            f.close()
            #2. Calculate Cumulative figures
            for i in range(len(data)):
                row_list =[];path_list = [];
                if i == 0 :
                    row_list.append(data[i][0])
                    path_list.append((data[i][0],0))
                else:
                    for column in range(len(data[i])):
                        e = data[i][column]
                        try:
                            if column !=0:
                                left_parent = cumulative_data[i-1][column-1];
                            else:
                                left_parent = 0
                        except:
                            left_parent = 0
                            
                        try:
                            right_parent = cumulative_data[i-1][column]
                        except:
                            right_parent = 0
                        
                        row_list.append(e+ max(left_parent,right_parent))
                        path_list.append((e,max(left_parent,right_parent)))
                        
                #print(path_list)
                cumulative_data[i] = row_list
                path[i] = path_list
        
            max_path_sum = max(cumulative_data[len(data)-1]) #element on the last row with the highest cumulative value
            path_of_element(max_path_sum,len(data)-1)
            print(" + ".join(list(map(str, elements)))," = ",str(max_path_sum))
            break
        except IOError:
            print("Unable to find the file {}".format(filename))      


    
    
if __name__ == "__main__":
    main()

