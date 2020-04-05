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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_0002:
    def addTwoNumbers_1(self, l1, l2):
        n1 = 0
        i = 1
        while l1:
            n1 += l1.val * i
            i *= 10
            l1 = l1.next
        n2 = 0
        i = 1
        while l2:
            n2 += l2.val * i
            i *= 10
            l2 = l2.next
        n3 = n1 + n2
        a = ListNode(n3 % 10)
        c = a
        n3 = int(n3 / 10)
        while n3:
            b = ListNode(n3 % 10)
            n3 = int(n3 / 10)
            a.next = b
            a = b
        return c
    
    def test(self):
        a1 = ListNode(2)
        a2 = ListNode(4)
        a3 = ListNode(3)
        a1.next = a2
        a2.next = a3
        b1 = ListNode(5)
        b2 = ListNode(6)
        b3 = ListNode(4)
        b1.next = b2
        b2.next = b3
        # assert self.addTwoNumbers_1(a1, b1) == c1


if __name__ == '__main__':
    Solution_0001().test()
    Solution_0002().test()
