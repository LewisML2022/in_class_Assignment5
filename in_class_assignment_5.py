#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''

import random

def quicksort(content_list):

#WRITE YOUR CODE HERE FOR THE RECURSIVE SORTING FUNCTION
# Modified from https://www.koderdojo.com/blog/quicksort-algorithm-in-python
    def sort(lst, l, r):
        # base case
        if r <= l:
            return

        # choose random pivot
        pivot_index = random.randint(l, r)

        # move pivot to first index
        lst[l], lst[pivot_index] = lst[pivot_index], lst[l]

        # partition
        i = l
        for j in range(l+1, r+1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        # place pivot in proper position
        lst[i], lst[l] = lst[l], lst[i]

        # sort left and right partitions
        sort(lst, l, i-1)
        sort(lst, i+1, r)

    if content_list is None or len(content_list) < 2:
        return

    sort(content_list, 0, len(content_list) - 1)
    
    print('\nThe sorted list is: ', content_list)

def main():

# WRITE YOUR MAIN FUNCTION HERE TO READ IN YOUR numbers.txt FILE, RUN THE LIST THROUGH YOUR SORTING ALGORITHM, 
# AND WRITE OUT YOUR FILE
    # modified from https://appdividend.com/2021/06/21/how-to-read-file-into-list-in-python/   
    txt_file = open("numbers.txt", "r")
    file_content = txt_file.read()
    print("The file contents are: ", file_content)
    
    content_list = file_content.replace('[', '').replace(']','').replace(' ', '').split(",")
    txt_file.close()
    content_list = [int(i) for i in content_list]
    print("\nThe list is: ", content_list)
    
    sorted_list = open("sorted.txt", "w")
    sorted_list.write("\n".join(str(i) for i in content_list))
    
    return content_list #WHAT DOES IT RETURN?


if __name__ == "__main__":
    main()