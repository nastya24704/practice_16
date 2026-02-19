def get_common_courses(courses) -> set[str]:
    """
    Return a set of courses chosen by all students.

    :param courses: List of sets, where each set contains
                    courses chosen by one student.
    :return: Set of courses common to all students.
    """
    if not courses:
        return set()

    return set.intersection(*courses)


def main() -> None:
    """
    Read input data, compute common courses,
    and print their count.
    """
    students_count = int(input())
    students_courses = []

    for person in range(students_count):
        students_courses.append(set(input().split()))

    common_courses = get_common_courses(students_courses)
    print(len(common_courses))


if __name__ == "__main__":
    main()
