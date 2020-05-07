

class Math1():

    def __init__(self):
        self.my_num1 = 10
        self.my_num2 = 20

    def addition(self):
        return self.my_num1 + self.my_num2

    def subtraction(self):
        return self.my_num1 - self.my_num2


class Math_Plus(Math1):

    def __init__(self, my_num1=40, my_num2=90):
        self.my_num1 = my_num1
        self.my_num2 = my_num2

    def multiplication(self):
        return self.my_num1 * self.my_num2

    def division(self):
        return self.my_num1 / self.my_num2


if __name__ == "__main__":
    math1 = Math1()
    print(math1.addition()) #30
    print(math1.subtraction()) #-10
    
    math_plus = Math_Plus()
    print(math_plus.addition()) #130
    print(math_plus.subtraction()) #-50
    print(math_plus.multiplication()) #3600
    print(math_plus.division()) #0.-44444444