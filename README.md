Simulated Dam Water Flow Monitoring System
Student Name: Richard S. Cartera
Student Number: 2601292
Section: 1CPE-A

Project Description
  This program monitors simulated dam water flow readings stored alongside their respective recording dates. It classifies each flow volume as NORMAL, WARNING, or CRITICAL based on specific thresholds and prints a detailed numerical summary with overall system status.

Features
- View all stored water flow readings with corresponding dates
- Add a new flow reading (0 to 100,000 ML/day) and date
- Classify every reading into NORMAL, WARNING, or CRITICAL levels
- Generate a comprehensive numerical summary (Total, Average, Min, Max, and Category Counts) and overall status
- Input error handling for invalid menu choices and invalid numerical ranges

Requirements
  Python 3 (no external packages required)

How to Run
  Open a terminal inside your project folder.
  
Type: python device_monitor.py
(On macOS or Linux, type: python3 device_monitor.py)

```SIMULATED DAM WATER FLOW MONITORING SYSTEM
------------------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: 1

Current Readings:
-------------------
Reading 1: 28 ML/day on 2025-10-12
Reading 2: 1030 ML/day on 2026-10-13
Reading 3: 1500 ML/day on 2026-10-14
Reading 4: 370 ML/day on 2026-10-15
Reading 5: 500 ML/day on 2026-10-16
Reading 6: 700 ML/day on 2026-10-17

Enter "1" to return to the main menu or "2" to exit: 1
```
Known Limitations
- Readings and dates are stored in-memory, meaning they are lost when the program closes.
- The date input accepts any string format without strict validation for calendar accuracy (e.g., leap years or valid days).

Reflection
The hardest part of this project was refactoring the program architecture to completely eliminate global variables and transition to a strictly modular design where data is shared exclusively through function parameters and return values. During this process, I fixed scope and data-flow bugs where independent functions could not properly access, track, or update state variables like readings and dates. This was resolved by initializing the data structures locally inside main() and passing them explicitly into functions like view_readings, add_reading, and generate_summary, alongside implementing dedicated helper functions with return values for totals, averages, percentages, and classifications. Next time, I would improve the design by using object-oriented programming with classes to encapsulate data and behaviors together, making state management even more robust and scalable.
