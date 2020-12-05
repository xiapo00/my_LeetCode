from tester import tester


class Solution_0011:
    def maxArea_1(self, height: list) -> int: # timeout!!!
        if len(height) == 1:
            return 0
        maybe = []
        for i, h_i in enumerate(height):
            for j, h_j in enumerate(height[i + 1:]):
                maybe.append(min(h_i, h_j) * (j + 1))
        return max(maybe)
    
    def maxArea_2(self, height: list) -> int: # systematically wrong!!! not in func_set of test()
        if len(height) == 1:
            return 0
        elif len(height) == 2:
            return min(height)
        maybe = []
        h_s = height.copy()
        h_s.sort()
        h_s.reverse()
        i_max = len(h_s)
        i = 0
        while i < i_max:
            if i < i_max - 1 and h_s[i] == h_s[i + 1]:
                target = h_s[i]
                flag = False
                for j, item in enumerate(height):
                    if item == target:
                        if not flag:
                            left = j
                            flag = True
                        else:
                            right = j
                maybe.append((right - left) * target)
                while i < i_max - 1 and h_s[i + 1] == target:
                    i += 1
            elif i < i_max - 1 and h_s[i] != h_s[i + 1]:
                target_1 = h_s[i]
                target_2 = h_s[i + 1]
                flag = False
                for j, item in enumerate(height):
                    if item == target_1 or item == target_2:
                        if not flag:
                            left = j
                            flag = True
                            if item == target_1:
                                target_1 = target_2
                            else:
                                target_2 = target_1
                        else:
                            right = j
                maybe.append((right - left) * h_s[i + 1])
                i += 1
            else:
                i += 1
        return max(maybe)
    
    def maxArea_3(self, height: list) -> int: # timeout!!!
        if len(height) == 1:
            return 0
        elif len(height) == 2:
            return min(height)
        result = min(height[0], height[1])
        for i, item in enumerate(height[2 : ]):
            for j, h in enumerate(height[0 : i + 2]):
                if (i + 2 - j) * min(h, item) > result:
                    result = (i + 2 - j) * min(h, item)
        return result
    
    def maxArea_4(self, height: list) -> int:
        if len(height) == 1:
            return 0
        elif len(height) == 2:
            return min(height)
        i = 0
        j = len(height) - 1
        maybe = []
        while i != j:
            maybe.append((j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max(maybe)
    
    def maxArea_5(self, height: list) -> int:
        if len(height) == 1:
            return 0
        elif len(height) == 2:
            return min(height)
        i = 0
        j = len(height) - 1
        result = min(height[0], height[-1]) * j
        while i != j:
            if (j - i) * min(height[i], height[j]) > result:
                result = (j - i) * min(height[i], height[j])
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return result

    def test(self):
        func_set = [self.maxArea_1, self.maxArea_3, self.maxArea_4, self.maxArea_5]
        test_set = [(([1, 8, 6, 2, 5, 4, 8, 3, 7], ), [49, ]),
                    (([1, 2, 1], ), [2, ]),
                    (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ), [25, ])]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()


class Solution_0012:
    def intToRoman_1(self, num: int) -> str:
        converter = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        s = ''
        while num:
            for item in converter.keys():
                if num // item:
                    s += converter[item] * (num // item)
                    num %= item
                    break
        s = s.replace('DCCCC', 'CM')
        s = s.replace('CCCC', 'CD')
        s = s.replace('LXXXX', 'XC')
        s = s.replace('XXXX', 'XL')
        s = s.replace('VIIII', 'IX')
        s = s.replace('IIII', 'IV')
        return s

    def test(self):
        func_set = [self.intToRoman_1, ]
        test_set = [((3, ), ["III", ]),
                    ((4, ), ["IV", ]),
                    ((9, ), ["IX", ]),
                    ((58, ), ["LVIII", ]),
                    ((1994, ), ["MCMXCIV", ])]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()


class Solution_0013:
    def romanToInt_1(self, s: str) -> int:
        converter = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s.replace('IV', 'IIII')
        s = s.replace('IX', 'VIIII')
        s = s.replace('XL', 'XXXX')
        s = s.replace('XC', 'LXXXX')
        s = s.replace('CD', 'CCCC')
        s = s.replace('CM', 'DCCCC')
        sum = 0
        for item in s:
            sum += converter[item]
        return sum

    def test(self):
        func_set = [self.romanToInt_1, ]
        test_set = [(("III", ), [3, ]),
                    (("IV", ), [4, ]),
                    (("IX", ), [9, ]),
                    (("LVIII", ), [58, ]),
                    (("MCMXCIV", ), [1994, ])]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()


class Solution_0014:
    def longestCommonPrefix_1(self, strs: list) -> str:
        if not strs:
            return ''
        result = strs[0]
        for item in strs:
            while item[0 : len(result)] != result:
                result = result[0 : len(result) - 1]
        return result

    def test(self):
        func_set = [self.longestCommonPrefix_1, ]
        test_set = [((["flower","flow","flight"], ), ["fl", ]),
                    ((["dog","racecar","car"], ), ["", ])]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()


class Solution_0015:
    def threeSum_1(self, nums: list) -> list:
        def twoSum(nums: list, target: int) -> list:
            d = {}
            result = []
            for index, item in enumerate(nums):
                if item in d.keys():
                    result.append([item, target - item, -target])
                else:
                    d[target - item] = index
            return result
        
        if set(nums) == {0} and len(nums) > 2:
            return [[0, 0, 0], ]
        result = []
        for i, item in enumerate(nums):
            L2 = twoSum(nums[0 : i] + nums[i + 1 :], -item)
            if L2:
                result += L2
        result = sorted(list(map(sorted, result)))
        if not result:
            return []
        L = [result[0]]
        for item in result:
            if item != L[-1]:
                L.append(item)
        return L
    
    def threeSum_2(self, nums: list) -> list: # timeout
        if len(nums) < 3:
            return []
        nums.sort()
        result = []
        for j in range(1, len(nums)-1):
            i, k = j - 1, j + 1
            while True:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    if i == 0 and k == len(nums) - 1:
                        break
                    i = i - 1 if i > 0 else i
                    k = k + 1 if k < len(nums) - 1 else k
                elif nums[i] + nums[j] + nums[k] > 0:
                    if i > 0:
                        i -= 1
                    else:
                        break
                else:
                    if k < len(nums) - 1:
                        k += 1
                    else:
                        break
        if not result:
            return []
        L = [result[0]]
        for item in result:
            if item not in L:
                L.append(item)
        return L
    
    def test(self):
        func_set = [lambda x: sorted(list(map(sorted, self.threeSum_1(x)))),
                    lambda x: sorted(list(map(sorted, self.threeSum_2(x))))]
        test_set = [(([-1, 0, 1, 2, -1, -4], ), [sorted(list(map(sorted, [[-1, 0, 1], [-1, -1, 2]]))), ]),
                    (([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6], ), [sorted(list(map(sorted, [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]))), ])]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()


class Solution_0016:
    def threeSumClosest_1(self, nums: list, target: int) -> int: # timeout
        result = nums[0]+nums[1]+nums[2]
        if len(nums) == 3:
            return result
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if abs(nums[i]+nums[j]+nums[k]-target) < abs(result-target):
                        result = nums[i]+nums[j]+nums[k]
        return result
    
    def threeSumClosest_2(self, nums: list, target: int) -> int: # Unfinished
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        result = sum(nums[0:4])
        for j in range(1, len(nums)-1):
            i, k = j - 1, j + 1
            while True:
                if abs(nums[i] + nums[j] + nums[k] - target) < result:
                    result = abs(nums[i] + nums[j] + nums[k] - target)
        return result

    def test(self):
        func_set = [self.threeSumClosest_1, ]
        test_set = [(([-1, 2, 1, -4], 1), [2, ]), ]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()


class Solution_0017:
    def letterCombinations_1(self, digits: str) -> list:
        if not digits:
            return []
        
        def listCombine(l1: list, l2: str) -> list:
            result = []
            for item1 in l1:
                for item2 in l2:
                    result.append(item1 + item2)
            return result

        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = ['']
        for digit in digits:
            result = listCombine(result, mapping[digit])
        return result

    def test(self):
        func_set = [self.letterCombinations_1, ]
        test_set = [(("23", ), [["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], ]), ]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution_0018:
    def removeNthFromEnd_1(self, head: ListNode, n: int) -> ListNode:
        needle = head
        l = 0
        while needle:
            needle = needle.next
            l += 1
        if l == n:
            head = head.next
            return head
        needle = head
        for i in range(l - n - 1):
            needle = needle.next
        needle.next = needle.next.next
        return head

    def removeNthFromEnd_2(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        needle = head
        L = []
        for i in range(n+1):
            L.append(needle)
            try:
                needle = needle.next
            except AttributeError:
                return head.next
        while L[-1].next:
            L = list(map(lambda x: x.next, L))
        if n == 1:
            L[-2].next = None
            return head
        L[0].next = L[2]
        return head
    
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
        
        func_set = [lambda x, y: ListNode2int(self.removeNthFromEnd_1(x, y)), lambda x, y: ListNode2int(self.removeNthFromEnd_2(x, y))]
        for f in func_set:
            test_set = [((int2ListNode(54321), 2), [5321, ]),
                        ((int2ListNode(1), 1), [0, ]),
                        ((int2ListNode(21), 1), [1, ]),
                        ((int2ListNode(21), 2), [2, ])]
            for data in test_set:
                tester(f, *data).test()


if __name__ == '__main__':
    class_set = [eval('Solution_%04d' % (x)) for x in range(11, 19)]
    [S().test() for S in class_set]
