from itertools import combinations


def get_all_subsets(numbers) -> list[tuple[int, ...]]:
    """
    Return all subsets of the given set.

    :param numbers: List of natural numbers.
    :return: List of all subsets.
    """
    numbers = sorted(numbers)
    subsets = []

    for r in range(len(numbers) + 1):
        subsets.extend(combinations(numbers, r))

    return subsets


def main() -> None:
    numbers = list(map(int, input().split()))
    result = get_all_subsets(numbers)

    for subset in result:
        print(*subset)


if __name__ == "__main__":
    main()
