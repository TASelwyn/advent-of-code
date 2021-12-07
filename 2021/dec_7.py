# Thomas Selwyn
# 07-Dec-2021

answers = [0, 0]

# Read data input
with open('data/day_7.txt') as data_file:
    crab_positions = [int(i) for i in data_file.read().split(",")]
    data_file.close()

print(crab_positions)

crab_range = range(min(crab_positions), max(crab_positions) + 1)
fuel_spent = [[0] * len(crab_range), [0] * len(crab_range)]

for x in crab_range:
    for i in range(len(crab_positions)):
        change_x = abs(x - crab_positions[i])
        fuel_spent[0][x] += change_x
        fuel_spent[1][x] += int(change_x * (change_x + 1) / 2)


print(fuel_spent[0])
print(fuel_spent[1])

answers[0] = min(fuel_spent[0])
answers[1] = min(fuel_spent[1])

print("***" * 15)
print(f"Final answer for Part One is {answers[0]}")
print(f"Final answer for Part Two is {answers[1]}")
print("***" * 15)
