from tester import tester


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
        func_set = [self.twoSum_1, self.twoSum_2]
        test_set = [(([3, 2, 4], 6), [[1, 2], ]), ]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()


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

        func_set = [lambda x, y: ListNode2int(self.addTwoNumbers_1(x, y)), lambda x, y: ListNode2int(self.addTwoNumbers_2(x, y))]
        test_set = [((int2ListNode(932), int2ListNode(149)), [1081, ]), ]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()


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
        func_set = [self.lengthOfLongestSubstring_1, ]
        test_set = [(('ggububgvfk', ), [6, ]), ]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()


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

    def test(self):
        func_set = [self.findMedianSortedArrays_1, self.findMedianSortedArrays_2]
        test_set = [(([1, 2, 5], [3, 4, 6]), [3.5, ]), ]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()


class Solution_0005:
    def longestPalindrome_1(self, s: str) -> str:
        if s == s[-1::-1]:
            return s
        else:
            L = []
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    if s[i: j] == s[i: j][-1::-1]:
                        L.append(s[i: j])
            return L[list(map(len, L)).index(max([item for item in map(len, L)]))]

    def longestPalindrome_2(self, s: str) -> str:
        if s == s[::-1]:  # This can filter out strings with 0 or 1 element or 2 repeated elements
            return s
        else:
            # find wanted son-strings with odd-numbered elements
            centre = 0
            radius = 0
            L = [s[0], '']
            while True:
                if s[centre + radius] == s[centre - radius]:
                    radius += 1
                else:
                    L[-1] = s[centre - radius + 1: centre + radius]
                    L.append('')
                    centre += 1
                    radius = 0
                if centre - radius < 0:
                    L[-1] = s[centre - radius + 1: centre + radius]
                    L.append('')
                    centre += 1
                    radius = 0
                if centre + radius >= len(s):
                    L[-1] = s[centre - radius + 1: centre + radius]
                    L.append('')
                    break
            # find wanted son-strings with even-numbered elements
            centre = 0
            radius = 0
            while True:
                if s[centre] == s[centre + 1]:
                    if s[centre - radius] == s[centre + radius + 1]:
                        radius += 1
                    else:
                        L[-1] = s[centre - radius + 1: centre + radius + 1]
                        L.append('')
                        centre += 1
                        radius = 0
                    if centre - radius < 0:
                        L[-1] = s[centre - radius + 1: centre + radius + 1]
                        L.append('')
                        centre += 1
                        radius = 0
                    if centre + radius + 1 >= len(s):
                        L[-1] = s[centre - radius + 1: centre + radius + 1]
                        L.append('')
                        break
                elif centre < len(s) - 2:
                    centre += 1
                else:
                    break
            return L[list(map(len, L)).index(max([item for item in map(len, L)]))]

    def test(self):
        func_set = [self.longestPalindrome_1, self.longestPalindrome_2]
        test_set = [(('babad', ), ['bab', 'aba']),
                    (('bb', ), ['bb', ]),
                    (('ac', ), ['a', 'c', ]),
                    (('2000001', ), ['00000', ])]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()


class Solution_0006:
    def convert_1(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        result = ''
        d = numRows * 2 - 2
        for i in range(numRows):
            for j, ch in enumerate(s):
                if j % d == i or j % d == d - i:
                    result += ch
        return result

    def convert_2(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        L = ['', ] * numRows
        d = numRows * 2 - 2
        for i, ch in enumerate(s):
            if i % d <= numRows - 1:
                L[i % d] += ch
            else:
                L[d - i % d] += ch
        result = ''
        for item in L:
            result += item
        return result

    def test(self):
        func_set = [self.convert_1, self.convert_2]
        test_set = [(("LEETCODEISHIRING", 3), ["LCIRETOESIIGEDHN", ]),
                    (("LEETCODEISHIRING", 4), ["LDREOEIIECIHNTSG", ]),
                    (("A", 1), ["A", ]),
                    (("AB", 1), ["AB", ])]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()


class Solution_0007:
    def reverse_1(self, x: int) -> int:
        if x > 2147483647 or x < -2147483648:
            return 0
        sign = (x >= 0) * 2 - 1
        x //= sign
        y = 0
        while x:
            y = y * 10 + x % 10
            x //= 10
        if y > 2147483647 or y < -2147483648:
            return 0
        return y * sign

    def reverse_2(self, x: int) -> int:
        if x > 2147483647 or x < -2147483648:
            return 0
        sign = (x >= 0)
        x = x if x >= 0 else -x
        y = 0
        while x:
            y = y * 10 + x % 10
            x //= 10
        if y > 2147483647 or y < -2147483648:
            return 0
        return y if sign else -y

    def reverse_3(self, x: int) -> int:
        if x > 2147483647 or x < -2147483648:
            return 0
        sign = (x >= 0)
        x = x if x >= 0 else -x
        y = int(str(x)[-1::-1])
        if y > 2147483647 or y < -2147483648:
            return 0
        return y if sign else -y

    def test(self):
        func_set = [self.reverse_1, self.reverse_2, self.reverse_3]
        test_set = [((123, ), [321, ]),
                    ((-123, ), [-321, ]),
                    ((120, ), [21, ]),
                    ((1534236469, ), [0, ])]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()


class Solution_0008:
    def myAtoi_1(self, str: str) -> int:
        if str.replace(' ', '') == '':
            return 0
        else:
            i = 0
            while str[i] == ' ':
                i += 1
            if str[i] in '+-1234567890':
                temp = str[i]
                i += 1
                while i < len(str) and str[i] in '1234567890':
                    temp += str[i]
                    i += 1
                return min(max(int(temp), -2147483648), 2147483647) if temp != '+' and temp != '-' else 0
            else:
                return 0

    def test(self):
        func_set = [self.myAtoi_1, ]
        test_set = [(('42', ), [42, ]),
                    (('   -42', ), [-42, ]),
                    (('4193 with words', ), [4193, ]),
                    (('-91283472332', ), [-2147483648, ]),
                    (('+', ), [0, ])]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()


class Solution_0009:
    def isPalindrome_1(self, x: int) -> bool:
        if x < 0:
            return False
        y = 0
        xc = x
        while xc:
            y = y * 10 + xc % 10
            xc //= 10
        return x == y

    def isPalindrome_2(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def test(self):
        func_set = [self.isPalindrome_1, self.isPalindrome_2]
        test_set = [((121, ), [True, ]),
                    ((-121, ), [False, ]),
                    ((10, ), [False, ])]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()


class Solution_0010:
    def isMatch_1(self, s: str, p: str) -> bool:
        import re
        return bool(re.match('^%s$' % (p, ), s))

    def isMatch_2(self, s: str, p: str) -> bool: # Unfinished
        i_max, j_max = len(s) - 1, len(p) - 1
        i, j = 0, 0
        while i <= i_max and j <= j_max:
            if s[i] == p[j] or p[j] == '.':
                i, j = i + 1, j + 1
            elif p[j] == '*':
                if s[i] == p[j - 1] or p[j - 1] == '.':
                    i += 1
                elif s[i] == p[j + 1] or p[j + 1] == '.':
                    j += 1
                else:
                    return False
            elif p[j + 1] == '*':
                j += 2
            else:
                return False
        if j > j_max and j - j_max != i - i_max:
            return False
        return True

    def test(self):
        func_set = [self.isMatch_1, self.isMatch_2]
        test_set = [(("aa", "a"), [False, ]),
                    (("aa", "a*"), [True, ]),
                    (("ab", ".*"), [True, ]),
                    (("aab", "c*a*b"), [True, ]),
                    (("mississippi", "mis*is*p*."), [False, ]),
                    (("mississippi", "mis*is*ip*."), [True, ]),
                    (("ab", ".*c"), [False, ]),
                    (("ab", ".*c*"), [True, ])]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()


if __name__ == '__main__':
    class_set = [eval('Solution_%04d' % (x + 1)) for x in range(10)]
    [S().test() for S in class_set]
