def is_in_intersection(first_set, second_set, value) -> bool:
    """
    Check whether a value belongs to the intersection
    of two sets.

    :param first_set: First set of integers.
    :param second_set: Second set of integers.
    :param value: Integer value to check.
    :return: True if value is in the intersection,
             otherwise False.
    """
    intersection = first_set & second_set
    return value in intersection


def main() -> None:
    """
    Read input data, check membership in the intersection,
    and print the result.
    """
    first_set = set(map(int, input().split()))
    second_set = set(map(int, input().split()))
    value = int(input())

    print(is_in_intersection(first_set, second_set, value))


if __name__ == "__main__":
    main()
