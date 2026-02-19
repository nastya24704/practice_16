from itertools import combinations


def get_k_subsets(numbers, k) -> list[tuple[int, ...]]:
    """
    Return all k-element subsets.

    :param numbers: List of natural numbers.
    :param k: Size of subset.
    :return: List of k-element subsets.
    """
    return list(combinations(sorted(numbers), k))


def main() -> None:
    numbers = list(map(int, input().split()))
    k = int(input())

    result = get_k_subsets(numbers, k)

    for subset in result:
        print(*subset)


if __name__ == "__main__":
    main()
