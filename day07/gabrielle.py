import numpy as np
import matplotlib.pyplot as plt
from math import inf

with open("input.txt", "r") as f:
    line = f.readline()

crabs = [int(crab) for crab in line.split(",")]

min_crab = min(crabs)
max_crab = max(crabs)

min_fuel = inf
for i in range(min_crab, max_crab+1):
    fuel = 0
    for crab in crabs:
        fuel += abs(i-crab)
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)

min_fuel = inf
for i in range(min_crab, max_crab+1):
    fuel = 0
    for crab in crabs:
        diff = abs(i-crab)
        fuel += diff*(diff+1)/2
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)