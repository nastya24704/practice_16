def find_repeated_numbers(numbers) -> set[int]:
    """
    Return a set of numbers that occur more than once.
    """
    repeated = set()
    for number in numbers:
        if numbers.count(number) > 1:
            repeated.add(number)
    return repeated


def is_in_repeated(numbers, figure) -> bool:
    """
    Check whether the figure belongs to repeated numbers.
    """
    repeated_numbers = find_repeated_numbers(numbers)
    return figure in repeated_numbers


def main() -> None:
    numbers = list(map(int, input().split()))
    figure = int(input())
    print(is_in_repeated(numbers, figure))


if __name__ == "__main__":
    main()
