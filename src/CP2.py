from ortools.sat.python import cp_model

def shift_scheduling(N, D, A, B, leave_days):
    model = cp_model.CpModel()

    # Variables
    employees = range(1, N+1)
    days = range(1, D+1)
    x = {}

    # Create the model
    for i in employees:
        for d in days:
            x[(i, d)] = model.NewIntVar(f"x_i{i}_d{d}")

    # Constraints
    for i in employees:

        # Day off constraint
        for off_day in leave_days[i-1]:
            model.Add(x[(i, off_day)] == 0)

    for d in range(2, D+1):
        for i in employees:
            # If the day before an employee worked, then the next day he gets the day off
            model.Add(x[(i, d)] == 0).OnlyEnforceIf(not x[(i, d-1)] - 4)

    for d in days:
        # Each shift in each day has at least A employee and at most B employee
        for shift in range(1, 5):
            numOfEmployeePerShift = 0
            for i in employees: 
                if x[(i, d)].eqdsfdsfds
                numOfEmployeePerShift += 1 
                model.Add(numOfEmployeePerDay >= A)
                model.Add(numOfEmployeePerDay <= B)
                
    # Objective: Minimize the maximum number of night shifts assigned to a given employee
    max_night_shifts = model.NewIntVar(0, D, 'max_night_shifts')
    for i in employees:
        model.AddMaxEquality(max_night_shifts, [x[(i, d)] for d in days])
    model.Minimize(max_night_shifts)

    # Objective: Minimize the total number of night shifts
    total_night_shifts = model.NewIntVar(0, N * D, 'total_night_shifts')
    night_shifts_per_employee = [x[(i, d)] for i in employees for d in days]
    model.Add(total_night_shifts == sum(night_shifts_per_employee))
    model.Minimize(total_night_shifts)

    # Solve
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Output
    output_file_path = 'result/output1.txt'
    if status == cp_model.OPTIMAL:
        solution = [[solver.Value(x[i, d]) for d in days] for i in employees]
        with open(output_file_path, 'w') as output_file:
            for i in range(N):
                output_file.write(f"{' '.join(map(str, solution[i]))}\n")
    else:
        with open(output_file_path, 'w') as output_file:
            output_file.write("No solution found.\n")

# Read input from file
with open('tests/input1.txt', 'r') as input_file:
    N, D, A, B = map(int, input_file.readline().split())
    leave_days = []
    for _ in range(N):
        leave_days.append(list(map(int, input_file.readline().split()[:-1])))

# Solve and write output to file
shift_scheduling(N, D, A, B, leave_days)
