def find_repeated_numbers(numbers) -> set[int]:
    """ Return a set of numbers that occur more than once. """
    for number in numbers:
        if numbers.count(number) > 1:
            return number


def is_in_repeated(numbers, value) -> bool:
    """ Check whether the value belongs to the set of repeated
    numbers. """
    all_numbers = set()
    repeated = set()
    for number in numbers:
        if number in all_numbers:
            repeated.add(number)
        else:
            all_numbers.add(number)
    return value in repeated_numbers


def main() -> None:
    numbers = list(map(int, input().split()))
    value = int(input())
    print(is_in_repeated(numbers, value))

if __name__ == "__main__":
    main()
