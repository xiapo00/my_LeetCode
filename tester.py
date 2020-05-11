import re


class tester:
    def __init__(self, func, ques: tuple, answ: list):
        self.f = func
        self.x = ques
        self.y = answ
        try:
            self.name = re.findall('bound method (.*?) of <', str(func))[0]
        except IndexError:
            self.name = str(func)

    def test(self):
        result = self.f(*self.x)
        if result not in self.y:
            print(f'Inputting {self.x}, the result should be in {self.y}, but your function {self.name} returned {result}.')
