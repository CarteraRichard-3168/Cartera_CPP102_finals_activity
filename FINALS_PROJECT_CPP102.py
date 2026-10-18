from datetime import datetime

def main():
    # Data is initialized locally inside main() and passed around via parameters
    readings = [28, 1030, 1500, 370, 500, 700]
    dates = ["2025-10-12", "2026-10-13", "2026-10-14", "2026-10-15", "2026-10-16", "2026-10-17"]
    
    while True:
        print("SIMULATED DAM WATER FLOW MONITORING SYSTEM")
        print("------------------------------------------")
        print("[1] View Readings")
        print("[2] Add Reading")
        print("[3] Classify Readings")
        print("[4] Generate Summary")
        print("[5] Exit")
        print()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            view_readings(readings, dates)
        elif choice == "2":
            add_reading(readings, dates)
        elif choice == "3":
            classify_readings(readings)
        elif choice == "4":
            generate_summary(readings, dates)
        elif choice == "5":
            kill_program()
        else:
            print("Invalid choice. Please try again.\n")


def kill_program():
    print("Thank you for using the Device Monitoring System.")
    raise SystemExit


def view_readings(readings, dates):
    print("\nCurrent Readings:")
    print("-------------------")
    for water, (reading, date) in enumerate(zip(readings, dates), start=1):
        print(f"Reading {water}: {reading} ML/day on {date}")
    print()

    choice2 = input('Enter "1" to return to the main menu or "2" to exit: ')
    if choice2 == "2":
        kill_program()


def add_reading(readings, dates):
    while True:
        raw_input = input("Enter new reading: ").strip()
        if not raw_input:
            print("Invalid input. The reading cannot be empty.\n")
            continue
        try:
            new_reading = int(raw_input)
        except ValueError:
            print("Invalid input. Enter a whole number only.\n")
            continue
        if new_reading < 0 or new_reading > 100000:
            print("Invalid reading. Enter a value from 0 to 100000.\n")
            continue
        break

    while True:
        new_date = input("Enter date for the reading (YYYY-MM-DD): ").strip()
        if not new_date:
            print("Invalid input. The date cannot be empty.\n")
            continue
        try:
            parsed_date = datetime.strptime(new_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.\n")
            continue
        if parsed_date.year < 2020:
            print("Invalid date. Years before 2020 are not allowed.\n")
            continue
        break

    readings.append(new_reading)
    dates.append(new_date)
    print(f"Reading added successfully: {new_reading} ML/day on {new_date}\n")

    choice2 = input('Enter "1" to return to the main menu or "2" to exit: ')
    if choice2 == "2":
        kill_program()


def classify_single_reading(reading):
    if reading < 50:
        return "NORMAL"
    elif reading <= 500:
        return "WARNING"
    else:
        return "CRITICAL"


def classify_readings(readings):
    print("\nREADING CLASSIFICATION ")
    print("------------------------")
    for water, reading in enumerate(readings, start=1):  
        level = classify_single_reading(reading)  
        print(f"Reading {water}: {reading} ML/day -> {level}")
    print()

    choice2 = input('Enter "1" to return to the main menu or "2" to exit: ')
    if choice2 == "2":
        kill_program()


def calculate_total(readings):
    return sum(readings)


def calculate_average(readings):
    if not readings:
        return 0.0
    return sum(readings) / len(readings)


# Meets requirement: Returns a calculated number (percentage)
def calculate_percentage(part, total):
    if total == 0:
        return 0.0
    return (part / total) * 100


def get_overall_status(hi_count, norm_count):
    if hi_count >= 1:
        return "ATTENTION REQUIRED"
    elif norm_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def generate_summary(readings, dates):
    total = calculate_total(readings)       
    avg = calculate_average(readings)         
    highest = max(readings)
    lowest = min(readings)
    total_count = len(readings)
    
    low = 0
    norm = 0
    hi = 0
    for r in readings:
        lvl = classify_single_reading(r)
        if lvl == "NORMAL":
            low += 1
        elif lvl == "WARNING":
            norm += 1
        elif lvl == "CRITICAL":
            hi += 1

    # Calculate percentages using our new return function
    low_pct = calculate_percentage(low, total_count)
    norm_pct = calculate_percentage(norm, total_count)
    hi_pct = calculate_percentage(hi, total_count)

    status = get_overall_status(hi, norm)     

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"{'Number of readings':<18} : {total_count}")
    print(f"{'Total of readings':<18} : {total:.2f} ML/day")
    print(f"{'Average flow':<18} : {avg:.2f} ML/day")
    print(f"{'Maximum reading':<18} : {highest} ML/day")
    print(f"{'Minumum reading':<18} : {lowest} ML/day")
    print()
    print(f"{'NORMAL':<15} : {low} ({low_pct:.1f}%)")
    print(f"{'WARNING':<15} : {norm} ({norm_pct:.1f}%)")
    print(f"{'CRITICALLY HIGH':<15} : {hi} ({hi_pct:.1f}%)")
    print(f"Overall Status  : {status}\n")

    choice2 = input('Enter "1" to return to the main menu or "2" to exit: ')
    if choice2 == "2":
        kill_program()



main()