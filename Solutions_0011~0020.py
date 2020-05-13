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


if __name__ == '__main__':
    class_set = [eval('Solution_%04d' % (x)) for x in range(11, 15)]
    [S().test() for S in class_set]
