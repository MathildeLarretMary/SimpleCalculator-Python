# module to get aplhabet
import string

# put all alphabeth into a list
alphabet = list(string.ascii_letters)

"""_summary_
"""
# print(numbers)

class Calc:
    def __init__(self) -> None:
        # will take all calculations and results
        self.all_calc = {}

        while True:
            self.calculate()
            self.ask_again()

    def calculate(self):
        calc = input(" ---> ")
        elements = []
        result = ""
        # separate all elements of input
        for char in calc:
            elements.append(char)
        # check if a letter of alphabet is find on input
        if any(char in elements for char in alphabet):
            # if True :
            print("ValueError : You must use only numbers and operators ")
            return self.calculate()
        # if False :
        # get cacul to str
        result = eval(result.join(elements))
        # transform str value to obj -> calculate
        self.all_calc[f"{calc}"] = result
        print(result)
        
    def ask_again(self):
        answer = input("Do you want to continue ? ( Y / N ) -> ").lower()
        while True:
            if answer == 'y':
                break
            elif answer == 'n':
                # TODO: show caculs and all results --> self.all_calc
                print("Your calculations were :")
                for key, value in self.all_calc.items():
                    print("   ",key," -> ", value)
                exit(0)
            else: 
                return self.ask_again()


Calc()
