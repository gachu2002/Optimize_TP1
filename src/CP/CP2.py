from ortools.sat.python import cp_model

def shift_scheduling(N, D, A, B, leave_days):
    model = cp_model.CpModel()

    # Variables
    employees = range(1, N+1)
    days = range(1, D+1)
    shifts = range(1, 5)
    x = {}

    # Create the model
    for i in employees:
        for d in days:
            x[(i, d)] = model.NewIntVar(0, 4, f"x_i{i}_d{d}")
    
    # Constraints
    for i in employees:
        # Day off constraint
        for off_day in leave_days[i-1]:
            model.Add(x[(i, off_day)] == 0)

    # for d in range(2, D+1):
    #     for i in range(1, N+1):
    #         # If the day before an employee worked, then the next day he gets the day off
    #         condition_var = model.NewBoolVar(f"condition_i{i}_d{d}")
    #         model.Add(x[(i, d - 1)] == 4).OnlyEnforceIf(condition_var)
    #         model.Add(x[(i, d)] == 0).OnlyEnforceIf(condition_var.Not())

    for d in days:
    # Each shift in each day has at least A employee and at most B employee
        for shift in range(1, 5):
            shift_occupied = [model.NewBoolVar(f"shift_occupied_i{i}_d{d}_s{shift}") for i in employees]
            for i in employees:
                model.Add(x[(i, d)] == shift).OnlyEnforceIf(shift_occupied[i-1])
                model.Add(x[(i, d)] != shift).OnlyEnforceIf(shift_occupied[i-1].Not())

            model.Add(sum(shift_occupied) >= A)
            model.Add(sum(shift_occupied) <= B)


    # Objective: Minimize the maximum number of night shifts assigned to a given employee
    max_night_shifts = model.NewIntVar(0, D, 'max_night_shifts')
    for i in employees:
        model.AddMaxEquality(max_night_shifts, [x[(i, d)] for d in days])
    model.Minimize(max_night_shifts)

    # # Objective: Minimize the total number of night shifts
    # total_night_shifts = model.NewIntVar(0, N * D, 'total_night_shifts')
    # night_shifts_per_employee = [x[(i, d)] for i in employees for d in days]
    # model.Add(total_night_shifts == sum(night_shifts_per_employee))
    # model.Minimize(total_night_shifts)
    
    # Solve
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    
    # Output
    output_file_path = 'tests\CPresult\out_N_8_D_6.txt'
    if status == cp_model.OPTIMAL:
        solution = [[solver.Value(x[i, d]) for d in days] for i in employees]
        with open(output_file_path, 'w') as output_file:
            for i in range(N):
                output_file.write(f"{' '.join(map(str, solution[i]))}\n")
    else:
        with open(output_file_path, 'w') as output_file:
            output_file.write("No solution found.\n")


# Read input from file
with open('res\in_N_8_D_6.txt', 'r') as input_file:
    N, D, A, B = map(int, input_file.readline().split())
    leave_days = []
    for _ in range(N):
        leave_days.append(list(map(int, input_file.readline().split()[:-1])))

# Solve and write output to file
shift_scheduling(N, D, A, B, leave_days)
