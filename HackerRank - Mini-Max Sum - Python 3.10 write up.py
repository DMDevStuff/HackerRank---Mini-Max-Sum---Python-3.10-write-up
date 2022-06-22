##    Given five positive integers, find the minimum and maximum values that
##    can be calculated by summing exactly four of the five integers. Then
##    print the respective minimum and maximum values as a single line of two
##    space-separated long integers.

##### ##### ##### #####

#   Iterative solution
#   O(n)
#   n is the length of integer_array
#   The Algorithm:
#       Iterate through the array
#       At each step keep track of the sum,
#       the smallest integer found so far,
#       the largest integer found so far.
#       Finish by printing sum - largest, sum - smallest
#   solution found in one pass through array

def solutionOne(integer_array):

    array_sum = integer_array[0]
    largest_element = integer_array[0]
    smallest_element = integer_array[0]

    for index in range(1, len(integer_array)):

        array_sum += integer_array[index]

        if integer_array[index] > largest_element:
            largest_element = integer_array[index]

        if integer_array[index] < smallest_element:
            smallest_element = integer_array[index]

    print(array_sum - largest_element, array_sum - smallest_element)

    return None

##### ##### ##### #####
