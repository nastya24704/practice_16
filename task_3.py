def get_unique_sweet_products(sweet_preferences,
    friends_preferences) -> set[str]:
    """
    Return products liked only by SweetTooth.

    :param sweet_preferences: Set of products liked by SweetTooth.
    :param friends_preferences: List of sets of products liked by friends.
    :return: Set of products liked only by SweetTooth.
    """
    if not friends_preferences:
        return sweet_preferences

    friends_union = set.union(*friends_preferences)
    return sweet_preferences - friends_union


def main() -> None:
    """
    Read input data, compute products liked only by SweetTooth,
    and print their count.
    """
    sweet_preferences = set(input().split())
    friends_count = int(input())
    friends_preferences = []

    for _ in range(friends_count):
        friends_preferences.append(set(input().split()))
    unique_products = get_unique_sweet_products(sweet_preferences,
        friends_preferences)
    print(len(unique_products))


if __name__ == "__main__":
    main()
