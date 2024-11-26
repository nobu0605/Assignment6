import sys
import json

# Function to validate user input (comma-separated integers)
def validate_input(input_str):
    try:
        # Splitting the input string and converting to integers
        numbers = [int(num.strip()) for num in input_str.split(",")]
        return numbers
    except ValueError:
        # If invalid input is provided, return an error message in JSON format
        print(json.dumps({"error": "Invalid input. Please enter a comma-separated list of integers."}))
        sys.exit()

# Function to perform bitwise operations
def bitwise_operations(numbers):
    if not numbers:
        # If the list is empty, return an error
        return {"error": "No integers provided."}

    # Initializing bitwise operations with the first number
    bitwise_and = numbers[0]
    bitwise_or = numbers[0]
    bitwise_xor = numbers[0]

    # Applying bitwise operations on the list of numbers
    for num in numbers[1:]:
        bitwise_and &= num
        bitwise_or |= num
        bitwise_xor ^= num

    # Returning the results as a dictionary
    return {
        "and": bitwise_and,
        "or": bitwise_or,
        "xor": bitwise_xor
    }

# Function to filter numbers greater than a threshold
def filter_numbers(numbers, threshold):
    try:
        # Converting the threshold to an integer
        threshold = int(threshold)
        # Filtering numbers using list comprehension
        filtered = [num for num in numbers if num > threshold]
        return filtered
    except ValueError:
        # If the threshold is invalid, return an error
        print(json.dumps({"error": "Invalid threshold value."}))
        sys.exit()

# Entry point for the script
if __name__ == "__main__":
    # Retrieving command-line arguments passed from the PHP script
    args = sys.argv
    if len(args) != 3:
        # Ensure both integers and threshold are provided
        print(json.dumps({"error": "Invalid arguments. Provide integers and a threshold."}))
        sys.exit()

    integers_input = args[1]
    threshold_input = args[2]

    # Validate and process the input
    numbers = validate_input(integers_input)
    bitwise_results = bitwise_operations(numbers)
    filtered_numbers = filter_numbers(numbers, threshold_input)

    # Combine results into a single response
    result = {
        "bitwise": bitwise_results,
        "filtered": filtered_numbers
    }

    # Print the result as JSON for the PHP script to capture
    print(json.dumps(result))
