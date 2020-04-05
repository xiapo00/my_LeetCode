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
        a = ListNode(n3 % 10)  # create new linked list
        c = a  # get the head of the list
        n3 //= 10
        while n3:
            b = ListNode(n3 % 10)  # create new node
            n3 //= 10
            a.next = b  # put the new node into the linked list
            a = b  # change the operating pointer
        return c
    
    def addTwoNumbers_2(self, l1, l2):
        up = False
        head_node = ListNode(0)
        n_node = head_node
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            n_node.val = n1 + n2 + up - 10 if n1 + n2 + up >= 10 else n1 + n2 + up
            up = (n1 + n2 + up >= 10)
            n_node.next = ListNode(1) if up or (l1 and l1.next) or (l2 and l2.next) else None
            n_node = n_node.next
            l1 = l1.next if l1 and l1.next else 0
            l2 = l2.next if l2 and l2.next else 0
        return head_node
    
    def test(self):
        def int2ListNode(n):
            a = ListNode(n % 10)
            c = a
            n //= 10
            while n:
                b = ListNode(n % 10)
                n //= 10
                a.next = b
                a = b
            return c

        def ListNode2int(l):
            n = 0
            i = 1
            while l:
                n += l.val * i
                i *= 10
                l = l.next
            return n
        
        n1, n2 = 932, 149
        assert ListNode2int(self.addTwoNumbers_1(int2ListNode(n1), int2ListNode(n2))) == n1 + n2
        assert ListNode2int(self.addTwoNumbers_2(int2ListNode(n1), int2ListNode(n2))) == n1 + n2


if __name__ == '__main__':
    Solution_0001().test()
    Solution_0002().test()
