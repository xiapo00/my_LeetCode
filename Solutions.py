class Solution_0001:
    def twoSum_1(self, nums: list, target: int) -> list:
        for (index_1, item_1) in enumerate(nums):
            for (index_2, item_2) in enumerate(nums[index_1 + 1:]):
                if item_1 + item_2 == target:
                    return [index_1, index_2 + index_1 + 1]

    def twoSum_2(self, nums: list, target: int):
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
    def addTwoNumbers_1(self, l1: ListNode, l2: ListNode) -> ListNode:
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

    def addTwoNumbers_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        up = False
        head_node = ListNode(0)
        n_node = head_node
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            n_node.val = n1 + n2 + up - 10 if n1 + n2 + up >= 10 else n1 + n2 + up
            up = (n1 + n2 + up >= 10)
            n_node.next = ListNode(1) if up or (
                l1 and l1.next) or (l2 and l2.next) else None
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
        assert ListNode2int(self.addTwoNumbers_1(
            int2ListNode(n1), int2ListNode(n2))) == n1 + n2
        assert ListNode2int(self.addTwoNumbers_2(
            int2ListNode(n1), int2ListNode(n2))) == n1 + n2


class Solution_0003:
    def lengthOfLongestSubstring_1(self, s: str) -> int:
        i = 0
        j = (s != '')
        while j < len(s):
            if s[j] not in s[i: j] and len(set(s[i: j])) == j - i:
                j += 1
            else:
                i += 1
                j += 1
        return j - i

    def test(self):
        assert self.lengthOfLongestSubstring_1("ggububgvfk") == 6


class Solution_0004:
    def findMedianSortedArrays_1(self, nums1: list, nums2: list) -> float:
        if not nums1:
            return (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1 + (len(nums2) % 2)]) / 2
        if not nums2:
            return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1 + (len(nums1) % 2)]) / 2
        i, j = 0, 0
        L = []
        while i + j < len(nums1) + len(nums2):
            if i < len(nums1) and (j >= len(nums2) or nums1[i] < nums2[j]):
                L.append(nums1[i])
                i += 1
            else:
                L.append(nums2[j])
                j += 1
        return (L[len(L) // 2] + L[len(L) // 2 - 1 + (len(L) % 2)]) / 2

    def findMedianSortedArrays_2(self, nums1: list, nums2: list) -> float:
        L = sorted(nums1 + nums2)
        return (L[len(L) // 2] + L[len(L) // 2 - 1 + (len(L) % 2)]) / 2
        # half = len(L) // 2
        # return (L[half] + L[~half]) / 2

    def test(self):
        assert self.findMedianSortedArrays_1([1, 2, 5], [3, 4, 6]) == 3.5
        assert self.findMedianSortedArrays_2([1, 2, 5], [3, 4, 6]) == 3.5


class Solution_0005:
    def longestPalindrome(self, s: str) -> str:
        if s == s[-1::-1]:
            return s
        else:
            L = []
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    if s[i: j] == s[i: j][-1::-1]:
                        L.append(s[i: j])
            return L[list(map(len, L)).index(max([item for item in map(len, L)]))]

    def test(self):
        assert self.longestPalindrome('babad') in ['bab', 'aba']
        assert self.longestPalindrome('bb') == 'bb'


if __name__ == '__main__':
    Solution_0001().test()
    Solution_0002().test()
    Solution_0003().test()
    Solution_0004().test()
    Solution_0005().test()
