from itertools import permutations


def solve_equation() -> None:
    """
    Print all solutions of the cryptarithm:
    ХОД + ХОД + ХОД = МАТ.
    """
    digits = range(10)

    for perm in permutations(digits, 5):
        x, o, d, m, a = perm
        t = (3 * (100 * x + 10 * o + d)) % 10

        hod = 100 * x + 10 * o + d
        mat = 100 * m + 10 * a + t

        if 3 * hod == mat and x != 0 and m != 0:
            print(f"{hod}+{hod}+{hod}={mat}")


if __name__ == "__main__":
    solve_equation()
