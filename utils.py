"""
This class is a calculator that performs arithmatic oparation on two numbers.

complete methods below and add missing methods according to the tests.

"""


class Calculator:
    """rounding_digits is a default value by which
    the calculator rounds off numbers 10/3 = 3.3333333333...
    if rounding_digits = 2 the answer for this expression is 3.33
    """

    rounding_digits = 0

    def __init__(self, round_digits):
        self.rounding_digits = round_digits

    def addtion(self, a, b):
        return self._round(a + b, self.rounding_digits)

    def subtraction(self, a, b):
        return self._round(a - b, self.rounding_digits)

    def multiplication(self, a, b):
        return self._round(a * b, self.rounding_digits)

    def division(self, a, b):
        return self._round(a / b, self.rounding_digits)

    @property
    def round_digits(self):
        return self.rounding_digits

    def set_round_digits(self, digits):
        self.rounding_digits = digits

    @staticmethod
    def _round(answer: float, decimal: int | None = None) -> float:
        if decimal is not None and isinstance(decimal, int) and decimal > 0:
            return round(answer, decimal)
        return answer


class History:
    def __init__(self, filepath="History.txt"):
        self.filepath_ = filepath

    def __init__(self, filepath):
        self.filepath_ = filepath

    def save(self, expression: str):
        with open(self.filepath_, "a", encoding="utf-8", errors="ignore") as file:
            file.write(expression + "\n")

    def restore(self) -> list[str]:
        try:
            with open(self.filepath_, "r", encoding="utf-8", errors="ignore") as file:
                return [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            return []

    def clear(self):
        with open(self.filepath_, "w", encoding="utf-8", errors="ignore"):
            pass
