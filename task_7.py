from itertools import permutations


def get_permutations(numbers) -> list[tuple[int, ...]]:
    """
    Return all permutations in lexicographic order.

    :param numbers: List of natural numbers.
    :return: List of permutations.
    """
    return list(permutations(sorted(numbers)))


def main() -> None:
    numbers = list(map(int, input().split()))
    result = get_permutations(numbers)

    for perm in result:
        print(*perm)


if __name__ == "__main__":
    main()
