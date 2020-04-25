import re


class tester:
    def __init__(self, func, ques: tuple, answ: list):
        self.f = func
        self.x = ques
        self.y = answ
        self.name = re.findall('bound method (.*?) of <', str(func))[0]

    def test(self):
        if self.f(*self.x) not in self.y:
            print(f'Inputting {self.x}, the result should be in {self.y}, but your function {self.name} returned {self.f(*self.x)}.')
