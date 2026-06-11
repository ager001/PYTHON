# ==========================================
# STUDENT GRADE ANALYZER
# ==========================================

import csv


def read_grades(filename="grades.csv"):
    """
    Reads grades from a CSV file and returns a list of grades.
    """
# Empty list to store valid grades
    grades = []
# This is an exception handling block to catch file not found errors and invalid data formats
    try:
        with open(filename, "r", encoding="utf-8") as file:
            
            reader = csv.reader(file)

            # Skip header row
            next(reader, None)

            for row in reader:
                if not row:
                    continue

                try:
                    name, grade = row
                    grade = int(grade)

                    if grade < 0 or grade > 100:
                        print(f"Invalid grade skipped: {grade}")
                        continue

                    grades.append(grade)
                except ValueError:
                    print(f"Invalid row skipped: {row}")

    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

    return grades

def count_students(grades):
    """
    Returns the total number of students.
    """
    return len(grades)


def calculate_mean(grades):
    """
    Returns the average grade.
    """
    if not grades:
        return 0

    return sum(grades) / len(grades)


def calculate_median(grades):
    """
    Returns the median grade.
    """

    if not grades:
        return 0

    sorted_grades = sorted(grades)

    n = len(sorted_grades)

    if n % 2 == 0:

        middle1 = sorted_grades[n // 2 - 1]
        middle2 = sorted_grades[n // 2]

        return (middle1 + middle2) / 2

    return sorted_grades[n // 2]


def highest_grade(grades):
    """
    Returns the highest grade.
    """
    if not grades:
        return 0

    return max(grades)


def lowest_grade(grades):
    """
    Returns the lowest grade.
    """
    if not grades:
        return 0

    return min(grades)
def grade_distribution(grades):
    """
    Returns the letter-grade distribution.
    """

    distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for grade in grades:

        if grade >= 90:
            distribution["A"] += 1

        elif grade >= 80:
            distribution["B"] += 1

        elif grade >= 70:
            distribution["C"] += 1

        elif grade >= 60:
            distribution["D"] += 1

        else:
            distribution["F"] += 1

    return distribution

def print_report(grades):
    """
    Prints a formatted student report.
    """

    if not grades:
        print("No grade data available.")
        return

    distribution = grade_distribution(grades)

    print("\n" + "=" * 40)
    print("      STUDENT GRADE REPORT")
    print("=" * 40)

    print(f"Total Students : {count_students(grades)}")
    print(f"Mean Grade     : {calculate_mean(grades):.2f}")
    print(f"Median Grade   : {calculate_median(grades)}")
    print(f"Highest Grade  : {highest_grade(grades)}")
    print(f"Lowest Grade   : {lowest_grade(grades)}")

    print("\nLetter Grade Distribution")
    print("-" * 25)

    for grade, count in distribution.items():
        print(f"{grade} : {count}")

    print("=" * 40)


def main():
    """
    Main program execution.
    """

    filename = "grades.csv"

    grades = read_grades(filename)

    print_report(grades)


if __name__ == "__main__":
    main()