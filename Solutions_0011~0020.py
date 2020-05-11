from tester import tester


class Solution_0011:
    def maxArea_1(self, height: list) -> int:
        pass

    def test(self):
        func_set = [self.maxArea_1, ]
        test_set = [(([1, 8, 6, 2, 5, 4, 8, 3, 7], ), [49, ]), ]
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


if __name__ == '__main__':
    class_set = [eval('Solution_%04d' % (x)) for x in range(11, 14)]
    [S().test() for S in class_set]
