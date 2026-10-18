| Test | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Six readings : 28, 1030, 1500, 370, 500, 700 | 
Current Readings:
-------------------
Reading 1: 28 ML/day on 2025-10-12
Reading 2: 1030 ML/day on 2026-10-13
Reading 3: 1500 ML/day on 2026-10-14
Reading 4: 370 ML/day on 2026-10-15
Reading 5: 500 ML/day on 2026-10-16
Reading 6: 700 ML/day on 2026-10-17

Enter "1" to return to the main menu or "2" to exit:  | | |
| TC02 | Choose 2, enter 450, enter 2026-10-18 | Displays Reading added successfully: 450 ML/day on 2026-10-18 and returns to menu option. | | |
| TC03 | Choose 2, enter abc | Rejects input with Invalid input. Enter a whole number only. | | |
| TC04 | Choose 2, enter -5 | Rejects input with Invalid reading. Enter a value from 0 to 100000. | | |
| TC05 | Choose 2, enter 150000 | Rejects input with Invalid reading. Enter a value from 0 to 100000. | | |
| TC06 | Choose 2, enter 300, enter 2026/13/45 | Rejects date with Invalid date format. Please use YYYY-MM-DD. | | |
| TC07 | Choose 2, enter 300, enter 2019-05-12 | Rejects date with Invalid date. Years before 2020 are not allowed. | | |
| TC08 | Choose 3 (using initial data) | READING CLASSIFICATION 
------------------------
Reading 1: 28 ML/day -> NORMAL
Reading 2: 1030 ML/day -> CRITICAL
Reading 3: 1500 ML/day -> CRITICAL
Reading 4: 370 ML/day -> WARNING
Reading 5: 500 ML/day -> WARNING
Reading 6: 700 ML/day -> CRITICAL

Enter "1" to return to the main menu or "2" to exit: | | |
| TC09 | Choose 4 (initial data) | MONITORING SUMMARY
------------------
Number of readings : 6
Total of readings  : 4128.00 ML/day
Average flow       : 688.00 ML/day
Maximum reading    : 1500 ML/day
Minumum reading    : 28 ML/day

NORMAL          : 1 (16.7%)
WARNING         : 2 (33.3%)
CRITICALLY HIGH : 3 (50.0%)
Overall Status  : ATTENTION REQUIRED

Enter "1" to return to the main menu or "2" to exit: | | |
| TC10 | Enter 9 | Displays Invalid choice. Please try again.| | |
| TC11 | Choose 5 | Displays Exiting program. | | |