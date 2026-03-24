#Bubble Sort in Python

def bubble_sort(list1):
    n = len(list1)
    for i in range(n):
        for j in range(0,n-i-1):
            if list1[j]>list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]


numList = [64, 34, 25, 12, 22, 11, 90]  #List of unsorted numbers
bubble_sort(numList)                    #Calling the function to sort the list
print("Sorted list is:", numList)       #Printing the sorted list

#===========================================================================================
#Insertion Sort in Python

