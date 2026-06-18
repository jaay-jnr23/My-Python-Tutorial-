import numpy as np

scores = np.array([
    [85, 90, 76],
    [92, 88, 79],
    [76, 95, 84],
    [89, 76, 93],
    [84, 87, 80]
])

highest_score = np.max(scores)

lowest_score = np.min(scores)

mean_score = np.mean(scores)

mean_deviation = np.mean(np.abs(scores - mean_score ))

print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("Mean Score:", mean_score)
print("Mean Deviaton:", mean_deviation)