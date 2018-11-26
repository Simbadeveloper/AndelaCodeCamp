import random
class primeNumbers:

    def __new__(cls, number):
        cls.validator(number)
        return cls.generate(number)

    ##Check if input is valid
    def validator(number):
        if type(number) is list or type(number) is dict:
            raise TypeError("Input cannot be of type list or dictionary")

    ##Generate prime numbers
    def generate(number):
        prime = []
        if number <= 0:
            return []
        else:
            for i in range(2, number+1):
                isPrime = True
                for j in range(2, i):
                    if i % j is 0:
                        isPrime = False

                if isPrime:
                    prime.append(i)
            return prime

