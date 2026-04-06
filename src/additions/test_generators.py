"""Generators.

Generators are functions that create iterators using a different approach than traditional
iterators. They use the 'yield' statement to pause execution and return values one at a time,
making them memory-efficient for large datasets or infinite sequences.

When an iteration begins using a for loop, the generator function runs until it reaches a
'yield' statement. At this point, it returns a value and pauses execution, maintaining its
state. The next iteration continues from where it left off.

Benefits:
- Memory efficiency: Values are generated on-demand rather than storing the entire sequence
- Lazy evaluation: Computation happens only when needed
- State preservation: Local variables and execution state are maintained between yields
- Simplified code: Often cleaner than implementing iterator classes

@see: https://www.learnpython.org/en/Generators
@see: https://docs.python.org/3/howto/functional.html#generators
"""

import random
from typing import Generator, Iterator, List, Optional, Tuple


def lottery(count: int = 3, min_val: int = 1, max_val: int = 10, 
            bonus_number: bool = True, bonus_min: int = 10, bonus_max: int = 20) -> Generator[int, None, None]:
    """Generate random lottery numbers.

    This generator function yields random integers simulating lottery numbers.
    It demonstrates how generators maintain state between yields and can produce
    values using different rules during iteration.

    Args:
        count: Number of regular lottery numbers to generate
        min_val: Minimum value for regular numbers (inclusive)
        max_val: Maximum value for regular numbers (inclusive)
        bonus_number: Whether to include a bonus number
        bonus_min: Minimum value for bonus number (inclusive)
        bonus_max: Maximum value for bonus number (inclusive)

    Yields:
        Random integers representing lottery numbers

    Examples:
        >>> for num in lottery(5, 1, 49, True, 1, 10):
        ...     print(num)
        23
        7
        42
        13
        31
        8  # bonus number
    """
    if min_val >= max_val or bonus_min >= bonus_max:
        raise ValueError("Maximum values must be greater than minimum values")
    
    if count < 0:
        raise ValueError("Count must be non-negative")
    
    # Generate regular lottery numbers
    for _ in range(count):
        yield random.randint(min_val, max_val)
    
    # Generate bonus number if requested
    if bonus_number:
        yield random.randint(bonus_min, bonus_max)


def unique_lottery(count: int = 6, min_val: int = 1, max_val: int = 49) -> Generator[int, None, None]:
    """Generate unique random lottery numbers.

    This generator yields unique random integers in the specified range,
    ensuring no duplicates (like in many real lottery systems).

    Args:
        count: Number of unique numbers to generate
        min_val: Minimum value (inclusive)
        max_val: Maximum value (inclusive)

    Yields:
        Unique random integers

    Raises:
        ValueError: If requested count exceeds available unique numbers
    """
    if count > (max_val - min_val + 1):
        raise ValueError(f"Cannot generate {count} unique numbers in range {min_val}-{max_val}")
    
    # Track numbers already generated to avoid duplicates
    used_numbers = set()
    
    while len(used_numbers) < count:
        num = random.randint(min_val, max_val)
        if num not in used_numbers:
            used_numbers.add(num)
            yield num


def fibonacci(limit: Optional[int] = None) -> Generator[int, None, None]:
    """Generate Fibonacci sequence numbers.

    This demonstrates how generators can create infinite sequences
    that would be impossible to store completely in memory.

    Args:
        limit: Maximum number of Fibonacci numbers to generate (None for infinite)

    Yields:
        Next number in the Fibonacci sequence
    """
    a, b = 0, 1
    count = 0
    
    while limit is None or count < limit:
        yield a
        a, b = b, a + b
        count += 1


def test_generators():
    """Test the generator functions."""
    # Test basic lottery function
    for number_index, random_number in enumerate(lottery()):
        if number_index < 3:
            assert 1 <= random_number <= 10, f"Regular number {random_number} out of range"
        else:
            assert 10 <= random_number <= 20, f"Bonus number {random_number} out of range"
    
    # Test with custom parameters
    custom_lottery = list(lottery(count=5, min_val=10, max_val=30, bonus_number=True, bonus_min=50, bonus_max=60))
    assert len(custom_lottery) == 6, f"Expected 6 numbers, got {len(custom_lottery)}"
    assert all(10 <= num <= 30 for num in custom_lottery[:5]), "Regular numbers out of range"
    assert 50 <= custom_lottery[5] <= 60, f"Bonus number {custom_lottery[5]} out of range"
    
    # Test unique lottery
    unique_numbers = list(unique_lottery())
    assert len(unique_numbers) == 6, f"Expected 6 numbers, got {len(unique_numbers)}"
    assert len(set(unique_numbers)) == 6, "Duplicate numbers found"
    
    # Test fibonacci
    fib_numbers = list(fibonacci(10))
    assert len(fib_numbers) == 10, f"Expected 10 numbers, got {len(fib_numbers)}"
    assert fib_numbers == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], f"Incorrect sequence: {fib_numbers}"
    
    print("All tests passed!")


if __name__ == "__main__":
    # Example usage
    print("Regular lottery (3 numbers + bonus):")
    for num in lottery():
        print(f"- {num}")
    
    print("\nUnique lottery numbers (6 unique numbers):")
    for num in unique_lottery():
        print(f"- {num}")
    
    print("\nFirst 10 Fibonacci numbers:")
    for i, num in enumerate(fibonacci(10)):
        print(f"{i+1}: {num}")
    
    # Run tests
    test_generators()