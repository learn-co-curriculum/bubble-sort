def bubble_sort(arr):

    is_sorted = False # Boolean flag to loop as many times as needed to sort arr

    while not is_sorted:
        is_sorted = True

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                # perform swap
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp

                is_sorted = False # reset Boolean flag to continue sort

    return arr

if __name__ == "__main__":
    print("Expecting: [1, 2, 3, 4]")
    print(bubble_sort([3, 2, 1, 4]))

    print("")

    print("Expecting: [1, 2, 3]")
    print(bubble_sort([1, 2, 3]))

    print("")

    print("Expecting: []")
    print(bubble_sort([]))

    print("")

    print("Expecting: [1, 2, 3]")
    print(bubble_sort([2, 3, 1]))

    print("")

    print("Expecting: [1]")
    print(bubble_sort([1]))

    print("")

    print("Expecting: [1, 3]")
    print(bubble_sort([3, 1]))

    print("")

    print("Expecting: [-2, 0, 0, 1, 5, 6, 6, 7, 8, 8]")
    print(bubble_sort([6, -2, 0, 8, 7, 8, 6, 0, 5, 1]))

# Please add your pseudocode to this file
##################################################################################
# initialize boolean sorted to false
#
# while sorted is false:
#   sorted = true
#   iterate over array with index tracking:
#     if current element is larger than next element:
#       swap those elements in place
#       sorted = false
#
# return input array
##################################################################################

# And a written explanation of your solution
##################################################################################
# Since we need to iterate over the array over and over until it's sorted, we need
# to track if it's sorted, so we initialize a Boolean to false to do exactly that.
# Next we need to use a while loop (or something similar) that runs until the Array
# is sorted. This allows us to iterate over the Array as many times as needed.
# Since we want to set sorted to false only if a swap happens, we'll set it to true
# before iterating over the Array. When we iterate over the Array, we always go
# over the whole thing. We compare the value we're iterating over to the next one, 
# and if the first one is more than the next one, we swap them. We also set sorted
# to false because of the swap. We'll eventually get to a point where there are no
# swaps and at that point, sorted will remain true and when the iteration ends,
# we'll exit the outer loop and return the Array.
# Big O for time complexity is O(n^2) quadratic time because of the loop within a loop. 
# In the worst case we'll end up going over the whole Array roughly once per element.
##################################################################################