readings = [28, 1030, 1500, 370, 500, 700]
dates = ["2025-10-12", "2026-10-13", "2026-10-14", "2026-10-15", "2026-10-16", "2026-10-17"]
choice = ""
low = 0
norm = 0
hi = 0

def main_menu():
    global choice
    print("SIMULATED DAM WATER FLOW MONITORING SYSTEM")
    print("------------------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")
    print()
    choice = input("Enter choice: ")

    if choice == "1":
        view_readings()
    elif choice == "2":
        add_reading()
    elif choice == "3":
        classify_readings()
    elif choice == "4":
        generate_summary()
    elif choice == "5":
        kill_program()
    else:
        print("Invalid choice. Please try again.\n")
        main_menu()


def kill_program():
    print("Exiting program.")
    raise SystemExit


def view_readings():
    print("\nCurrent Readings:")
    print("-------------------")
    for i, (reading, date) in enumerate(zip(readings, dates), start=1):
        print(f"Reading {i}: {reading} ML/day on {date}")
    print()

    choice2 = input('Enter "1" to return to the main menu or "2" to exit: ')
    if choice2 == "1":
        main_menu()
    elif choice2 == "2":
        kill_program()
    else:
        print("Invalid option. Returning to main menu.\n")
        main_menu()


def add_reading():
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
            print("Invalid reading. Enter a value from 0 to 100.\n")
            continue
        break

    new_date = input("Enter date for the reading (YYYY-MM-DD): ")
    readings.append(new_reading)
    dates.append(new_date)
    print(f"Reading added successfully: {new_reading} ML/day on {new_date}\n")

    choice2 = input('Enter "1" to return to the main menu or "2" to exit: ')
    if choice2 == "1":
        main_menu()
    elif choice2 == "2":
        kill_program()
    else:
        print("Invalid option. Returning to main menu.\n")
        main_menu()

def classify_readings():
    global low, norm, hi
    
    print("\nREADING CLASSIFICATION ")
    print("------------------------")
    
    for i, reading in enumerate(readings, start=1):  
        if reading < 50:
            level = "NORMAL"
            low += 1
        elif reading <= 500:
            level = "WARNING"
            norm += 1
        else:
            level = "CRITICAL"
            hi += 1
        print(f"Reading {i}: {reading} ML/day -> {level}")

    choice2 = input('Enter "1" to return to the main menu or "2" to exit: ')
    if choice2 == "1":
        main_menu()
    elif choice2 == "2":
        kill_program()
    else:
        print("Invalid option. Returning to main menu.\n")
        main_menu()


def generate_summary():
    total = sum(readings)
    avg = total / len(readings)
    highest = max(readings)
    lowest = min(readings)
    
    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"{'Number of readings':<18} : {len(readings)}")
    print(f"{'Total of readings':<18} : {total:.2f} ML/day")
    print(f"{'Average flow':<18} : {avg:.2f} ML/day")
    print(f"{'Maximum reading':<18} : {highest} ML/day")
    print(f"{'Minumum reading':<18} : {lowest} ML/day")
    print()
    print(f"{'NORMAL':<15} : {low}")
    print(f"{'WARNING':<15} : {norm}")
    print(f"{'CRITICALLY HIGH':<15} : {hi}")

    if hi >= 1:
        print("Overall Status : ATTENTION REQUIRED")
    elif norm >= 1:
        print("Overall Status : MONITOR")
    else :
        print("Overall Status : NORMAL")

    choice2 = input('Enter "1" to return to the main menu or "2" to exit: ')
    if choice2 == "1":
        main_menu()
    elif choice2 == "2":
        kill_program()
    else:
        print("Invalid option. Returning to main menu.\n")
        main_menu()


while True:
    main_menu()

