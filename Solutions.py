class Solution_0001:
    def twoSum_1(self, nums, target):
        for (index_1, item_1) in enumerate(nums):
            for (index_2, item_2) in enumerate(nums[index_1 + 1:]):
                if item_1 + item_2 == target:
                    return [index_1, index_2 + index_1 + 1]

    def twoSum_2(self, nums, target):
        d = {}
        for index, item in enumerate(nums):
            if item in d.keys():
                return [d[item], index]
            else:
                d[target - item] = index

    def test(self):
        nums = [3, 2, 4]
        target = 6
        assert self.twoSum_1(nums, target) == [1, 2]
        assert self.twoSum_2(nums, target) == [1, 2]


if __name__ == '__main__':
    Solution_0001().test()
