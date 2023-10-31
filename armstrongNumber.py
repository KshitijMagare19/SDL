import itertools
def isArmstrong(n):
    i = n
    total = 0
    while i != 0:
        digit = i % 10
        total += digit ** 3
        i //= 10
    return total == n
class ArmstrongNumberFinder:
    def __init__(self, n):
        self.n = n
    def find_armstrong_numbers(self):
        for i in itertools.islice(itertools.count(1), self.n):
            if isArmstrong(i):
                print(i)
# Input the value of 'n'
n = int(input("Enter a number: "))
# Create an instance of the ArmstrongNumberFinder class and find Armstrong numbers
finder = ArmstrongNumberFinder(n)
print("Armstrong Numbers between 0 and "+ str(n) +" are :")
finder.find_armstrong_numbers()


