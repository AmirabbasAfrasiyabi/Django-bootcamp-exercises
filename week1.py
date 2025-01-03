# friday

"""
def calculate_middle_sums(arr):
    n = len(arr)
    total_sum = 0

    # Generate all permutations of the list
    permutations = get_permutations(arr)

    # Calculate the sum of the middle elements of all permutations
    for perm in permutations:
        middle_index = n // 2
        middle_element = perm[middle_index]
        total_sum += middle_element
    return total_sum

def get_permutations(arr):
    if len(arr) <= 1:
        return [arr]

    result = []
    for i in range(len(arr)):
        current_element = arr[i]
        remaining_elements = arr[:i] + arr[i+1:]
        for permutation in get_permutations(remaining_elements):
            result.append([current_element] + permutation)
    return result


# Read input from the user
input_numbers = input().split()
input_numbers = [int(num) for num in input_numbers]

# Call the function and print the result
result =calculate_middle_sums(input_numbers)
print(result)
"""

# binary programming

"""
def generate_calculation(pattern):

    if '?' not in pattern :
        return [pattern]
    
    result = []

    index = pattern.index('?')
    for replacement in ['0','1'] :
        new_pattern = pattern[:index] + replacement + pattern[index+1:]

        result .extend(generate_calculation(new_pattern))
    
    return result

input_string = input()

output = generate_calculation(input_string)

print('\n'.join(output))

"""

#after and before (LByl - EAFP)


"""import math"""

# what id LBYL
"""
In this method, before executing code that may cause an error, preventive checks are performed to ensure that no error occurs.
"""

"""
def divide_LBYL(X,Y):

    if Y == 0 :
        return math.inf

    else:
        return X/Y

Number1 = int(input("please enter your number1 ->"))
Number2 = int(input("please enter your number2 ->"))
print("LYBL" , divide_LBYL(Number1,Number2) )
"""
    

#what is EAFP
"""
In this approach, instead of preventing errors, it is assumed that the code will execute without issues, and if an error occurs, the `try` and `except` block is used to handle it.
"""
"""def divide_EAFP(x,y):

    try:
        return x/y
    except ZeroDivisionError :
        return math.inf

Number1 = int(input("please enter your number1 ->"))
Number2 = int(input("please enter your number2 ->"))

print("EAFP" , divide_EAFP(Number1 , Number2))

"""

#alice
"""
import re
def process_logs(logs):
    log_pattern = re.compile(r'\[(\d{4}-\d{2}-\d{2} \d{1,2}:\d{2}:\d{2})\] (\w+): (.+)')
    log_dict = {}

    for log in logs:
        match = log_pattern.match(log)
        if match:
            timestamp, log_level, message = match.groups()

            # Extract year and hour from the timestamp
            year = timestamp[:4]
            hour = timestamp[11:13]

            # Create a key for the log in the dictionary
            key = f'Year {year}, Hour {hour}'

            # Initialize the log_dict entry if not exists
            if key not in log_dict:
                log_dict[key] = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}

            # Increment the corresponding log level count
            log_dict[key][log_level] += 1

    return log_dict

def print_logs(log_dict):
    for key, values in log_dict.items():
        print(f"{key}: INFO={values['INFO']}, WARNING={values['WARNING']}, ERROR={values['ERROR']}")


n = int(input())
logs = [input() for _ in range(n)]

log_dict = process_logs(logs)
print_logs(log_dict)
"""