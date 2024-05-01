import os


def extract_result(line: int) -> dict:
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'results.txt')

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if 0 <= line - 1 < len(lines):  # Check for valid line number
                coefficients_str = lines[line - 1].strip()[1:-1]  # Remove brackets and leading/trailing whitespaces
                coefficients = coefficients_str.split(',')
                return {
                    'coefficients': coefficients,
                    # 'average': float(lines[line].rstrip()),
                }
            else:
                return {}
    except FileNotFoundError:
        return {}


res = extract_result(1)

for i, coeff in enumerate(res['coefficients']):
    if float(coeff) > 2:
        print(i, coeff)
