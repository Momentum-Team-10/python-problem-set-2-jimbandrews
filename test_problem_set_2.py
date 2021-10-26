import pytest
import unittest
from problem_set_2 import (
    remove,
    sum_list,
    average,
    minimum,
    selection_sort,
    list_to_str,
)


class RemoveFromListTest(unittest.TestCase):
    def test_return_list_with_item_removed(self):
        test_list = ["Cadence", "Ordel", "Marion"]
        assert remove(test_list, "Marion") == ["Cadence", "Ordel"]

    def test_return_list_unchanged_if_item_not_found(self):
        test_list = ["Cadence", "Ordel", "Marion"]
        assert remove(test_list, "Riley") == test_list

    def test_remove_all_occurrences_of_item(self):
        assert remove(["Cadence", "Ordel", "Marion", "Cadence"], "Cadence") == [
            "Ordel",
            "Marion",
        ]

    def test_does_not_change_original_list(self):
        test_list = ["Cadence", "Ordel", "Marion"]
        remove(test_list, "Cadence")
        assert test_list == ["Cadence", "Ordel", "Marion"]


class SumListTest(unittest.TestCase):
    def test_returns_0_for_empty_list(self):
        assert sum_list([]) == 0

    def test_works_with_only_one_number_in_list(self):
        assert sum_list([5]) == 5

    def test_adds_all_numbers_in_list(self):
        assert sum_list([1, 2, 3, 4, 5]) == 15


class AverageListTest(unittest.TestCase):
    def test_returns_None_for_empty_list(self):
        assert average([]) == None

    def test_works_with_only_one_number_in_list(self):
        assert average([5]) == 5

    def test_returns_average_of_numbers_in_list(self):
        assert average([1, 2, 3, 4, 5]) == 3


class MinimumInListTest(unittest.TestCase):
    def test_returns_None_for_empty_list(self):
        assert minimum([]) == None

    def test_returns_the_number_for_an_array_with_only_one_number(self):
        assert minimum([1]) == 1

    def test_returns_the_minimum_number_in_an_array_of_numbers(self):
        assert minimum([2, 1, 3]) == 1

    def test_works_with_negative_integers(self):
        assert minimum([7, 31, -4, 2]) == -4


class SelectionSortTest(unittest.TestCase):
    def test_returns_empty_list_for_empty_list(self):
        assert selection_sort([]) == []

    def test_returns_the_same_list_for_list_with_one_item(self):
        assert selection_sort([2]) == [2]

    def test_returns_the_same_list_for_a_sorted_list(self):
        assert selection_sort([2, 4, 10, 12]) == [2, 4, 10, 12]

    def test_returns_a_sorted_list(self):
        assert selection_sort([4, 2, 12, 10]) == [2, 4, 10, 12]


class ListToStrTest(unittest.TestCase):
    def test_returns_empty_string_for_empty_string(self):
        assert list_to_str("") == ""

    def test_returns_string_with_no_commas_for_list_of_1_item(self):
        assert list_to_str(["Marion"]) == "Marion"

    def test_returns_string_with_comma_separated_list_items(self):
        assert list_to_str(["Cadence", "Ordel", "Marion"]) == "Cadence,Ordel,Marion"
