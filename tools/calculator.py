def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Lista vacía.")
    return sum(numbers) / len(numbers)
