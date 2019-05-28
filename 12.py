import random

NUM_POINTS = 30000

def estimate_pi(num_points):
    in_circle = 0
    for i in range(num_points):
        x = random.random()
        y = random.random()
        if x*x + y*y < 1:
            in_circle += 1

    return in_circle*4/num_points

print(estimate_pi(NUM_POINTS))