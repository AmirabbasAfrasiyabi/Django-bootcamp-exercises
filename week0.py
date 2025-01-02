#example 1 : anti virous


"""
import re
string =(input("please enter your string -> :)"))
res = re.search(r"^[a-zA-Z0-9]+\.([A-Za-z]{3})$" , string)
print("Warning") if res == None else print("OK")

"""


# example2 : Karname

"""def process_scores(scores):
    n = len(scores)

    # Validate the number of students
    if n < 1 or n > 1000:
        raise ValueError("The number of scores must be between 1 and 1000.")

    # Validate each score
    if not all(1 <= score <= 20 for score in scores):
        raise ValueError("All scores must be between 1 and 20.")

    # Calculate average score
    average = sum(scores) / n

    # Find the minimum and maximum scores
    min_score = min(scores)
    max_score = max(scores)

    # Calculate the total sum of scores
    total_sum = sum(scores)

    return round(average, 2), min_score, max_score, total_sum

# Input data
input_data = input("Enter the scores separated by space: ").strip()
scores = list(map(int, input_data.split()))

# Process the scores
try:
    average, min_score, max_score, total_sum = process_scores(scores)
    # Output the results with two decimal places for the average
    print(f"{average:.2f} {min_score} {max_score} {total_sum}")
except ValueError as e:
    print(e)
"""

# tabdil vahed
"""
def convert_units(value, from_unit, to_unit):
    # Conversion factors relative to meters
    conversion_factors = {
        "m": 1,
        "km": 0.001,
        "mi": 0.000621371
    }

    # Validate units
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid units. Supported units are: m, km, mi.")

    # Direct conversion using factors
    converted_value = value * conversion_factors[to_unit] / conversion_factors[from_unit]

    return converted_value

# Input data
input_data = input("Enter the value, from unit, and to unit separated by spaces: ").strip()
data_parts = input_data.split()

try:
    # Parse input
    n = float(data_parts[0])
    from_unit = data_parts[1]
    to_unit = data_parts[2]

    # Validate value range
    if n < 0 or n > 1000000:
        raise ValueError("Value must be between 0 and 1000000.")

    # Perform conversion
    result = convert_units(n, from_unit, to_unit)

    # Output the result with six decimal places
    print(f"{result:.6f}")
except (ValueError, IndexError) as e:
    print(f"Error: {e}")

"""

#asci table

"""
input_str = input()
ascii_list = [ord(char) for char in input_str]
print(ascii_list)
"""