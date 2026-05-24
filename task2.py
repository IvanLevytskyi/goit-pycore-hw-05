import re
from typing import Callable


def generator_numbers(text: str):
    # Regular expression for floating-point numbers
    pattern = r"\b\d+\.\d+\b"

    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable):
    # Calculate total sum of all numbers
    return sum(func(text))


# Example text
text = (
    "Employee income consists of several parts: "
    "1000.01 as the base income, supplemented by additional "
    "earnings of 27.45 and 324.00 dollars."
)

total_income = sum_profit(text, generator_numbers)

print(f"Total income: {total_income}")