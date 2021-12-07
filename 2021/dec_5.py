# Thomas Selwyn
# 05-Dec-2021

answers = [0, 0]
vector_lines = []
diagonal_vectors = []
thermal_vent_grid = [[0] * 1000 for j in range(1000)]
overlap_counter = 0

# Read data input
with open('data/day_5.txt') as data_file:
    read_lines = data_file.readlines()
    data_file.close()

    for current in read_lines:
        piece = [int(current.strip().split(" -> ")[i].split(",")[j]) for i in range(2) for j in range(2)]
        vector_lines.append([[piece[0], piece[1]], [piece[2], piece[3]]])

print(vector_lines)


def rangeBetweenTwoNumbers(number_one, number_two):
    return range(number_one, number_two + 1) if (number_one < number_two) \
        else range(number_two, number_one + 1)


def sortVectorByClosestToXAxis(current_vector):
    return [current_vector[0] if current_vector[0][0] < current_vector[1][0] else current_vector[1],
            current_vector[1] if current_vector[0][0] < current_vector[1][0] else current_vector[0]]


def PrintVectorOntoGrid(vector):
    global overlap_counter
    starting_pos = vector[0]
    ending_pos = vector[1]

    # Only continue horizontal/vertical lines
    if starting_pos[0] == ending_pos[0] or starting_pos[1] == ending_pos[1]:
        for x in rangeBetweenTwoNumbers(starting_pos[1], ending_pos[1]):
            for y in rangeBetweenTwoNumbers(starting_pos[0], ending_pos[0]):
                thermal_vent_grid[x][y] += 1

                if thermal_vent_grid[x][y] == 2:
                    overlap_counter += 1
    else:
        # Diagonal lines (Part Two, save data for later so we don't loop over part one vectors again)
        diagonal_vectors.append(vector)
        # print(vector)


def PrintDiagonalVector(vector):
    global overlap_counter
    global thermal_vent_grid
    # Sorting vector makes it exclusively diagonal & anti diagonal lines.
    sorted_vector = sortVectorByClosestToXAxis(vector)
    starting_pos, ending_pos = sorted_vector[0], sorted_vector[1]
    # print(sorted_vector)

    for x in range(abs(starting_pos[0] - ending_pos[0]) + 1):
        if starting_pos[0] < ending_pos[0] and starting_pos[1] < ending_pos[1]:
            thermal_vent_grid[starting_pos[1] + x][starting_pos[0] + x] += 1
            overlap_counter += 1 if (thermal_vent_grid[starting_pos[1] + x][starting_pos[0] + x] == 2) else 0
        else:
            thermal_vent_grid[starting_pos[1] - x][starting_pos[0] + x] += 1
            overlap_counter += 1 if (thermal_vent_grid[starting_pos[1] - x][starting_pos[0] + x] == 2) else 0


# Run over all vectors for part one
for vector in vector_lines:
    PrintVectorOntoGrid(vector)
answers[0] = overlap_counter

# Part two, loop over diagonal vectors that were prevented from running for part one
print(diagonal_vectors)
for diag_vector in diagonal_vectors:
    PrintDiagonalVector(diag_vector)
answers[1] = overlap_counter

print("***" * 15)
print(f"Final answer for Part One is {answers[0]}")
print(f"Final answer for Part Two is {answers[1]}")
print("***" * 15)
