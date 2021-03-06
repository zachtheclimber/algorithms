import unittest
from random import shuffle, randint
from statistics import median


# O(n) time/space partitioning
def quick_sort(nums: list) -> list:
    if len(nums) < 2:
        return nums
    pivot = nums[-1]
    higher, lower = [], []
    for num in nums[:-1]:
        if num >= pivot:
            higher.append(num)
        else:
            lower.append(num)
    return quick_sort(lower) + [pivot] + quick_sort(higher)


# O(n) time / O(1) space partitioning
def quick_sort_in_place(nums: list, start, finish) -> list:
    if start >= finish:
        return nums

    unknown = start
    greater = start
    for _ in range(start, finish):
        if nums[unknown] > nums[finish]:
            unknown += 1
        else:
            _swap(unknown, greater, nums)
            greater += 1
            unknown += 1

    _swap(greater, finish, nums)

    partition = greater
    quick_sort(nums, start, partition - 1)
    quick_sort(nums, partition + 1, finish)

    return nums


# O(n) time / O(1) space partitioning w/ improved pivot selection
def quick_sort(nums: list, start, finish) -> list:
    if start >= finish:
        return nums

    if finish - start > 5:
        _set_pivot(nums, start, finish)

    unknown = start
    greater = start
    for _ in range(start, finish):
        if nums[unknown] > nums[finish]:
            unknown += 1
        else:
            _swap(unknown, greater, nums)
            greater += 1
            unknown += 1

    _swap(greater, finish, nums)

    partition = greater
    quick_sort(nums, start, partition - 1)
    quick_sort(nums, partition + 1, finish)

    return nums


def _set_pivot(nums, start, finish):
    rand_index1, rand_index2, rand_index3 = 0, 0, 0

    while rand_index1 == rand_index2 or rand_index1 == rand_index3 \
            or rand_index2 == rand_index3:
        rand_index1 = randint(start, finish)
        rand_index2 = randint(start, finish)
        rand_index3 = randint(start, finish)

    values = {nums[rand_index1]: rand_index1,
              nums[rand_index2]: rand_index2,
              nums[rand_index3]: rand_index3}

    median_index = values[median(values)]
    _swap(median_index, finish, nums)


def _swap(index_1, index_2, nums):
    nums[index_1], nums[index_2] = nums[index_2], nums[index_1]
    return


class TestQuickSort(unittest.TestCase):
    def test_1(self):
        nums = [1]
        self.assertEqual(quick_sort(nums, 0, len(nums) - 1), [1])

    def test_two(self):
        nums = [2, 1]
        self.assertEqual(quick_sort(nums, 0, len(nums) - 1), [1, 2])

    def test_three(self):
        nums = [2, 1, 3]
        self.assertEqual(quick_sort(nums, 0, len(nums) - 1), [1, 2, 3])

    def test_small(self):
        nums = [2, 1, 3, 100, 7, 9, 16]
        self.assertEqual(quick_sort(nums, 0, len(nums) - 1), [1, 2, 3, 7, 9, 16, 100])

    def test_large(self):
        sorted_nums = list(range(100))
        shuffled_nums = sorted_nums.copy()
        shuffle(shuffled_nums)
        self.assertEqual(quick_sort(shuffled_nums, 0, len(sorted_nums) - 1), sorted_nums)


if __name__ == "__main__":
    unittest.main()
