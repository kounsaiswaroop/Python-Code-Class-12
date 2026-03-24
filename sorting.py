numList = [64, 34, 25, 12, 22, 11, 90]  #List of unsorted numbers

#Bubble Sort in Python

def bubble_sort(list1):
    n = len(list1)
    for i in range(n):
        for j in range(0,n-i-1):
            if list1[j]>list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]


bubble_sort(numList)                    #Calling the function to sort the list
print("Sorted list is:", numList)       #Printing the sorted list

#===========================================================================================

#Insertion Sort in Python

def insertion_sort(list1):
    n = len(list1)
    for i in range(1, n):
        check = list1[i]
        j = i-1
        while j>=0 and check<list1[j]:
            list1[j+1]=list1[j]
            j=j-1
        else:
            list1[j+1]=check

insertion_sort(numList)                    #Calling the function to sort the list
print("Sorted list is:", numList)          #Printing the sorted list