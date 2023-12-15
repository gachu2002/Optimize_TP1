# Optimize_TP1
There are N employees 1,2,..., N need to be assigned to work shifts for days 1, 2, ..., D. Each day is divided into 4 shifts: morning, noon, afternoon, night. Know that:
- Each day, an employee only works at most 1 shift
- If the day before an employee worked the night shift, then the next day he get the day off
- Each shift in each day has at least A employee and at most B employee
F(i): list of leave days of employee i
Develop a plan to arrange shifts for N employees so that:
The maximum number of night shifts assigned to a given employee is the minimum
A solution is represented by a matrix X[1..N][1..D] in which x[i][d] is the shift scheduled to staff i on day d (value 1 means shift morning; value 2 means shift afternoon; value 3 means shift evening; value 4 means shift night; value 0 means day-off)
Input
Line 1: contains 4 positive integers N, D, A, B (1 <= N <= 500, 1 <= D <= 200, 1 <= A <= B <= 500)
Line i + 1 (i = 1, 2, . . ., N): contains a list of positive integers which are the day off of the staff i (days are indexed from 1 to D), terminated by -1