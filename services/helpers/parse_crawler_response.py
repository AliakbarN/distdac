import re


def parse_crawler_response(direction_str: str) -> float:
    numbers = re.findall(r'[-+]?\d*\.\d+|\d+', direction_str)

    # Convert the extracted number to float
    return float(numbers[0])
