from agents import function_tool

@function_tool
def calculate_average(numbers: list[float]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list[float]): List of input numbers.

    Returns:
        float: Average of the list.
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")
    return sum(numbers) / len(numbers)
