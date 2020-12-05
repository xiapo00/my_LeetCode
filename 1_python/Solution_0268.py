from tester import tester

class Solution_0268:
    def missingNumber_2(self, nums: list) -> int:
        table = list(range(len(nums)+1))
        for item in nums:
            table[item] = 0
        return sum(table)
    
    def test(self):
        func_set = [self.missingNumber_2, ]
        test_set = [(([3, 0, 1], ), [2, ])]
        for f in func_set:
            for data in test_set:
                tester(f, *data).test()

if __name__ == '__main__':
    class_set = [eval('Solution_%04d' % (x)) for x in range(268, 269)]
    [S().test() for S in class_set]
