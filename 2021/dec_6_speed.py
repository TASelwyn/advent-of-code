# Thomas Selwyn
# 06-Dec-2021
# The Speed Version
from datetime import datetime

fish_day_count = [0] * 9

# Read data input
with open('data/day_6.txt') as data_file:
    for i in data_file.read().split(","):
        fish_day_count[int(i)] += 1
    data_file.close()

print(fish_day_count)


def progressFishyTheSpeedyWay():
    global fish_day_count
    mommy_fishes_birthing = fish_day_count[0]

    # Shift da fishy array (moves the mommy fishies closer to birthing)
    fish_day_count = fish_day_count[1:]

    # Reset mothers & Add da baby fishies
    fish_day_count[6] += mommy_fishes_birthing
    fish_day_count.append(mommy_fishes_birthing)


# Simulate 256 days the speedy way
for day in range(256):
    progressFishyTheSpeedyWay()
    print(f"Day {day + 1} simulation ran. Total count: {sum(fish_day_count)}")

print("***" * 20)
print(f"Final answer for 256 simualations is {sum(fish_day_count)} fishies")
print("***" * 20)
