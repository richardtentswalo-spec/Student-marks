import random

def generate_mark():
    return random.randint(0, 100)

def determine_result(mark):
    if mark >= 75:
        return "Distinction"
    elif mark >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    total = 0
    highest = 0
    lowest = 100

    distinctions = 0
    passes = 0
    fails = 0

    top_student = 0
    low_student = 0

    for student in range(1, 16):
        mark = generate_mark()
        result = determine_result(mark)

        print(f"Student {student} - Mark: {mark} - {result}")

        total += mark

        if result == "Distinction":
            distinctions += 1
        elif result == "Pass":
            passes += 1
        else:
            fails += 1

        if mark > highest:
            highest = mark
            top_student = student

        if mark < lowest:
            lowest = mark
            low_student = student

    average = total / 15

    print("\n--- SUMMARY ---")
    print("Highest mark:", highest, "(Student", top_student, ")")
    print("Lowest mark:", lowest, "(Student", low_student, ")")
    print("Average mark:", round(average, 2))
    print("Distinctions:", distinctions)
    print("Passes:", passes)
    print("Fails:", fails)

main()
