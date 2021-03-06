# 1. Create a function called "remove" that takes a list and an
# item to remove from the list, and returns a new list with that item removed.
# For example, `remove(['Cadence', 'Ordel', 'Marion'], 'Marion')` returns
# `['Cadence', 'Ordel']`.

# If the item is not in the list, return the list unchanged.
# If the item is in the list, remove all instances of it from the list.
def remove(list_input, item):
    list_copy = list_input.copy()
    if item in list_copy:
        while item in list_copy:
            list_copy.remove(item)
    return list_copy

# ------------------------------------------------------------------------------
# 2. Revisit your "remove" function. Make sure that it does not change the original
# list but instead returns a new list.


# ------------------------------------------------------------------------------
# 3. Create a function called "sum_list" that takes a list of numbers and
# returns the sum of those numbers. Write this function without using the
# built-in `sum()` function.
def sum_list(num_list):
    total = 0
    for number in num_list:
        total += number
    return total

# ------------------------------------------------------------------------------
# 4. Create a function called "average" that takes a list of numbers
# and returns the average of those numbers.
def average(num_list):
    if num_list == []:
        return None
    else:
        return sum_list(num_list) / len(num_list)


# ------------------------------------------------------------------------------
# 5. Create a function called "minimum" that takes a list of numbers and
# returns the smallest number in that list. Write this function without using the
# built-in `min()` function.
def minimum(num_list):
    if num_list == []:
        return None
    else:
        minimum = num_list[0]
        for number in num_list:
            if number < minimum:
                minimum = number
        return minimum

# ------------------------------------------------------------------------------
# 6. There are many techniques to sort lists (or arrays) in programming. Many programming
# languages include functions or methods that can do this for you. We are going to
# implement sorting ourselves, however.
#
# A "selection sort" is one of the most simple sorting algorithms. To implement it,
# you start with an unsorted list of numbers. You search the list and find the
# smallest number in the list. You then insert that number into a new list as the first
# item and remove it from the original list. You continue doing this until
# there are no numbers left in the original list.
#
# Create a function called "selection_sort" that takes a list of numbers and returns
# a sorted list using the selection sort algorithm described above.
#
# Note 1: Do not delete things from the original list. Instead, you
# should make a copy of it and delete items from the copy.
#
# To copy a list in Python use the `copy()` method:
#
# list_copy = list.copy()
#
#
# Note 2: Selection sort can be implemented using one list. Read the explanation at
# https://courses.cs.vt.edu/csonline/Algorithms/Lessons/SelectionSort/index.html
# to see how. This may make more sense to you.
def selection_sort(num_list):
    list_copy = num_list.copy()
    sorted_list = []
    while len(sorted_list) < len(num_list):
        least = minimum(list_copy)
        sorted_list.append(least)
        list_copy.remove(least)
    return sorted_list

# ------------------------------------------------------------------------------
# 7. Create a function called "list_to_str" that takes a list and joins its items
# into a string separated by commas. There do not need to be spaces after the commas.
#
# For example, `list_to_str(['Cadence', 'Ordel', 'Marion'])` results in the string
# `"Cadence,Ordel,Marion"`
def list_to_str(input_list):
    return ",".join(input_list)