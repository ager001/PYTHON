# ==========================================
# STUDENT GRADE ANALYZER
# ==========================================

def read_grades(filename="grades.csv"):
    """
    Reads grades from a CSV file and returns a list of grades.
    """

    grades = []

    try:
        with open(filename, "r") as file:

            # Skip header row
            next(file)

            for line in file:

                line = line.strip()

                if not line:
                    continue

                try:
                    name, grade = line.split(",")

                    grade = int(grade)

                    if grade < 0 or grade > 100:
                        print(f"Invalid grade skipped: {grade}")
                        continue

                    grades.append(grade)

                except ValueError:
                    print(f"Invalid row skipped: {line}")

    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

    return grades