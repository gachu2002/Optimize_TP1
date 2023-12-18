import random

def initialize_solution(N, D, shifts):
    solution = {}
    for i in range(1, N+1):
        for d in range(1, D+1):
            for s in shifts:
                solution[(i, d, s)] = 0  # Initialize shifts to 0

    for i in range(1, N+1):
        for off_day in random.sample(range(1, D+1), random.randint(1, D)):  # Randomly set off days
            solution[(i, off_day, 1)] = 1  # Set day shift to 1

    return solution

def is_valid(solution, N, D, A, B, shifts):
    for d in range(1, D+1):
        for s in shifts:
            if A > sum(solution[(i, d, s)] for i in range(1, N+1)) or sum(solution[(i, d, s)] for i in range(1, N+1)) > B:
                return False
    return True

def total_night_shifts(solution, N, D):
    return sum(solution[(i, d, 4)] for i in range(1, N+1) for d in range(1, D+1))

def shift_scheduling_greedy(N, D, A, B, leave_days):
    shifts = [1, 2, 3, 4]
    solution = initialize_solution(N, D, shifts)

    iterations = 1000  # Adjust the number of iterations based on your needs

    for _ in range(iterations):
        i = random.randint(1, N)
        d = random.randint(1, D)
        s = random.choice(shifts)

        # Flip the shift
        solution[(i, d, s)] = 1 - solution[(i, d, s)]

        if not is_valid(solution, N, D, A, B, shifts):
            # Revert the change if the solution becomes invalid
            solution[(i, d, s)] = 1 - solution[(i, d, s)]

    # Output
    output_file_path = 'tests\GRresult\out_N_8_D_6.txt'
    with open(output_file_path, 'w') as output_file:
        for i in range(1, N+1):
            output_file.write(f"{' '.join(map(str, [solution[(i, d, s)] * s for d in range(1, D+1) for s in shifts]))}\n")

    print(f"Total night shifts: {total_night_shifts(solution, N, D)}")

# Read input from file
with open('res\in_N_8_D_6.txt', 'r') as input_file:
    N, D, A, B = map(int, input_file.readline().split())
    leave_days = []
    for _ in range(N):
        leave_days.append(list(map(int, input_file.readline().split()[:-1])))

# Solve and write output to file
shift_scheduling_greedy(N, D, A, B, leave_days)
