import sys
import json

def validate_input(input_str):
    try:
        # Split the input string and convert to integers
        numbers = [int(num.strip()) for num in input_str.split(",")]
        return numbers
    except ValueError:
        print(json.dumps({"error": "Invalid input. Please enter a comma-separated list of integers."}))
        sys.exit()

def bitwise_operations(numbers):
    if not numbers:
        return {"error": "No integers provided."}

    # Perform bitwise operations
    bitwise_and = numbers[0]
    bitwise_or = numbers[0]
    bitwise_xor = numbers[0]

    for num in numbers[1:]:
        bitwise_and &= num
        bitwise_or |= num
        bitwise_xor ^= num

    return {
        "and": bitwise_and,
        "or": bitwise_or,
        "xor": bitwise_xor
    }

def filter_numbers(numbers, threshold):
    try:
        threshold = int(threshold)
        filtered = [num for num in numbers if num > threshold]
        return filtered
    except ValueError:
        print(json.dumps({"error": "Invalid threshold value."}))
        sys.exit()

if __name__ == "__main__":
    # Retrieve arguments passed from PHP
    args = sys.argv
    if len(args) != 3:
        print(json.dumps({"error": "Invalid arguments. Provide integers and a threshold."}))
        sys.exit()

    integers_input = args[1]
    threshold_input = args[2]

    numbers = validate_input(integers_input)
    bitwise_results = bitwise_operations(numbers)
    filtered_numbers = filter_numbers(numbers, threshold_input)

    # Combine results
    result = {
        "bitwise": bitwise_results,
        "filtered": filtered_numbers
    }

    # Output as JSON for PHP to capture
    print(json.dumps(result))
