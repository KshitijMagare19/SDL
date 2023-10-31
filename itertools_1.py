import itertools
class FizzBuzzGenerator:
    def __init__(self, n):
        self.n = n
    def generate1(self):
        for i in itertools.count(1, 1):
            if i == self.n + 1:
                break
            elif i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)             
    def generate2(self):
        numbers = itertools.islice(itertools.count(1), self.n)
        for i in numbers:
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
n = int(input("Enter a number: "))              # Input the value of 'n'
# Create an instance of the FizzBuzzGenerator class and generate the FizzBuzz sequence
generator = FizzBuzzGenerator(n)
generator.generate1()
# generator.generate2()