# module to get aplhabet
import string

"""_summary_
"""


class Calc:
    ALPHABET = list(string.ascii_letters)

    # __init__ job is to initialize instance variables.
    # it should not have more responsibility
    def __init__(self) -> None:
        # will take all calculations and results
        self.calculations_history = {}
        self.input = None
        self.result = None

    def run(self):
        while True:
            self._display_prompt()
            self._get_user_input()
            if not self._valid_input():
                print('You must use only numbers and operators ")')
                continue
            self._calculate()
            self._display_result()
            self._save_operation()
            if not self._continue():
                break
        self._display_history()
        exit(0)

    @staticmethod
    def _display_prompt():
        print('---> ', end='')

    def _get_user_input(self):
        self.input = input()

    def _calculate(self):
        self.result = eval(''.join(self.input))

    def _display_result(self):
        print(self.result)

    def _valid_input(self):
        return not any(char in self.input for char in Calc.ALPHABET)

    def _save_operation(self):
        self.calculations_history[f"{self.input}"] = self.result

    def _continue(self):
        answer = input("Do you want to continue ? ( Y / N ) -> ").lower()
        options = {'y': True, 'n': False}
        if answer not in options.keys():
            return self._continue()
        return options[answer]

    def _display_history(self):
        print("Your calculations were:")
        for key, value in self.calculations_history.items():
            print(f"{key} -> {value}")


Calc().run()
