##  [0001. 两数之和](https://leetcode-cn.com/problems/two-sum/)
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。<br>
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
```
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```
代码：
```python
import re


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
        ques_set_1 = [[3, 2, 4], ]
        ques_set_2 = [6, ]
        answ_set = [[[1, 2], ], ]
        func_set = [self.twoSum_1, self.twoSum_2]
        for f in func_set:
            for i, x in enumerate(ques_set_1):
                if f(x, ques_set_2[i]) not in answ_set[i]:
                    print('Inputting ' + str(x) + ',' + str(ques_set_2[i]) + ', the result should be in ' + str(answ_set[i]) + ', but your function "' + re.findall(
                        'bound method (.*?) of <', str(f))[0] + '" returned ' + str(f(x, ques_set_2[i])) + '.')
```

## [0002. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/)
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。<br>
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。<br>
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
```
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
```
代码：
```python
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
    
        ques_set_1 = [int2ListNode(932), ]
        ques_set_2 = [int2ListNode(149), ]
        answ_set = [[1081, ], ]
        func_set = [self.addTwoNumbers_1, self.addTwoNumbers_2]
        for f in func_set:
            for i, x in enumerate(ques_set_1):
                if ListNode2int(f(x, ques_set_2[i])) not in answ_set[i]:
                    print('Inputting ' + str(ListNode2int(x)) + ',' + str(ListNode2int(ques_set_2[i])) + ', the result should be in ' + str(answ_set[i]) + ', but your function "' + re.findall(
                        'bound method (.*?) of <', str(f))[0] + '" returned ' + str(ListNode2int(f(x, ques_set_2[i]))) + '.')
```
## [0003. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
```
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```
示例 2:
```
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```
示例 3:
```
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```
 代码：
```python
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
        ques_set = ['ggububgvfk', ]
        answ_set = [[6, ], ]
        func_set = [self.lengthOfLongestSubstring_1, ]
        for f in func_set:
            for i, x in enumerate(ques_set):
                if f(x) not in answ_set[i]:
                    print('Inputting ' + str(x) + ', the result should be in ' + str(answ_set[i]) + ', but your function "' + re.findall(
                        'bound method (.*?) of <', str(f))[0] + '" returned ' + str(f(x)) + '.')
```

## [0004.寻找两个有序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。<br>
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。<br>
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
```
nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
```
示例 2:
```
nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
```
代码：
```python
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
        ques_set_1 = [[1, 2, 5], ]
        ques_set_2 = [[3, 4, 6], ]
        answ_set = [[3.5, ], ]
        func_set = [self.findMedianSortedArrays_1, self.findMedianSortedArrays_2]
        for f in func_set:
            for i, x in enumerate(ques_set_1):
                if f(x, ques_set_2[i]) not in answ_set[i]:
                    print('Inputting ' + str(x) + ',' + str(ques_set_2[i]) + ', the result should be in ' + str(answ_set[i]) + ', but your function "' + re.findall(
                        'bound method (.*?) of <', str(f))[0] + '" returned ' + str(f(x, ques_set_2[i])) + '.')
```

## [0005. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
```
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
```
示例 2：
```
输入: "cbbd"
输出: "bb"
```
代码：
```python
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
        if s == s[-1::-1]:  # This can filter out strings with 0 or 1 element or 2 repeated elements
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
        ques_set = ['babad', 'bb', 'ac', '2000001']
        answ_set = [['bab', 'aba'], ['bb', ], ['a', 'c'], ['00000', ]]
        func_set = [self.longestPalindrome_1, self.longestPalindrome_2]
        for f in func_set:
            for i, x in enumerate(ques_set):
                if f(x) not in answ_set[i]:
                    print('Inputting ' + str(x) + ', the result should be in ' + str(answ_set[i]) + ', but your function "' + re.findall(
                        'bound method (.*?) of <', str(f))[0] + '" returned ' + str(f(x)) + '.')
```
## [0006. Z 字形变换](https://leetcode-cn.com/problems/zigzag-conversion/)
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。<br>
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
```
L   C   I   R
E T O E S I I G
E   D   H   N
```
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。<br>
请你实现这个将字符串进行指定行数变换的函数：<br>
string convert(string s, int numRows);

示例 1:
```
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
```
示例 2:
```
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
```
代码：
```python
class Solution_0006:
    # Unfinished
    def test(self):
        pass
```
## [0007. 整数反转](https://leetcode-cn.com/problems/reverse-integer/)
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
```
输入: 123
输出: 321
```
示例 2:
```
输入: -123
输出: -321
```
示例 3:
```
输入: 120
输出: 21
```
注意:<br>
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

代码：
```python
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
        ques_set = [123, -123, 120, 1534236469]
        answ_set = [[321, ], [-321, ], [21, ], [0, ]]
        func_set = [self.reverse_1, self.reverse_2, self.reverse_3]
        for f in func_set:
            for i, x in enumerate(ques_set):
                if f(x) not in answ_set[i]:
                    print('Inputting ' + str(x) + ', the result should be in ' + str(answ_set[i]) + ', but your function "' + re.findall(
                        'bound method (.*?) of <', str(f))[0] + '" returned ' + str(f(x)) + '.')
```
测试：
```python
if __name__ == '__main__':
    class_set = [eval('Solution_%04d' % (x + 1)) for x in range(7)]
    [S().test() for S in class_set]
```