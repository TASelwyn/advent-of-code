# Thomas Selwyn
# 06-Dec-2021

answers = [0, 0]

# Read data input
with open('data/day_6.txt') as data_file:
    data = [int(i) for i in data_file.read().split(",")]
    data_file.close()

print(data)

# Part One
fish_spawning_rates = data.copy()


def progressFishyTheVerySlowWay():
    for fish in range(len(fish_spawning_rates)):
        fish_spawning_rates[fish] -= 1

        if (fish_spawning_rates[fish]) == -1:
            fish_spawning_rates[fish] = 6
            fish_spawning_rates.append(8)


# Crunch the 80 day simulations
for day in range(80):
    progressFishyTheVerySlowWay()
    print(day + 1, len(fish_spawning_rates))
answers[0] = len(fish_spawning_rates)

# Part Two
# Parse fishies into one small "hashy" table
fish_day_count = [0] * 9
for i in range(len(data)):
    fish_day_count[data[i]] += 1


def progressFishyTheSpeedyWay():
    global fish_day_count
    mommy_fishes_birthing = fish_day_count[0]

    # Shift da fishy array (moves the mommy fishies closer to birthing)
    fish_day_count = fish_day_count[1:]
    fish_day_count.append(0)

    # Reset mothers & Add da fishies
    fish_day_count[6] += mommy_fishes_birthing
    fish_day_count[8] += mommy_fishes_birthing


# Simulate 256 days the speedy way
for day in range(256):
    progressFishyTheSpeedyWay()
    print(day + 1, sum(fish_day_count))

answers[1] = sum(fish_day_count)
print("***" * 15)
print(f"Final answer for Part One is {answers[0]}")
print(f"Final answer for Part Two is {answers[1]}")
print("***" * 15)
