from tester import tester


class Solution_0013:
    def romanToInt_1(self, s: str) -> int:
        converter = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
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
    Solution_0013().test()
