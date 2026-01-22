import numpy as np

array = np.array(1.50)
print(array)  # Output: 1.5

array = np.array(3.60)
result = np.multiply(array, 3)
print(result)  # Output: 10.8

array_5s = np.full((6, 6), 5)
print(array_5s)


arr = np.array([1, 24])
print(np.shape(arr))  # Output: (1, 2)
print(arr.size)       # Output: 2

arr = np.arange(24)
reshaped_arr = arr.reshape(4, 6)
print(reshaped_arr)

arr = np.array([1, 24])
print(arr > 20)

arr = np.array([4, 7, 12, 15, 20, 23, 24])
divisible_by_4 = arr[arr % 4 == 0]
print("Numbers divisible by 4:", divisible_by_4)


# Initialize the scores array
scores = np.array([45, 60, 75, 90, 30, 85])

# 1. Find and print the average score
average = np.mean(scores)
print(f"Average score: {average}")

# 2. Count how many scores are >= 60
count_passing = np.sum(scores >= 60)
print(f"Scores >= 60: {count_passing}")

# 3. Replace scores below 60 with 60
scores[scores < 60] = 60
print(f"Updated scores: {scores}")


# Initialize the scores array
scores = np.array([45, 60, 75, 90, 30, 85])

# 1. Find and print the average score
average = np.mean(scores)
print(f"Average score: {average}")

# 2. Count how many scores are >= 60
count_passing = np.sum(scores >= 60)
print(f"Scores >= 60: {count_passing}")

# 3. Replace scores below 60 with 60
scores[scores < 60] = 60
print(f"Updated scores: {scores}")


# Initialize the array
arr = np.array([10, 20, 30, 40, 50])

# 1. Statistical analysis
print(f"Min: {np.min(arr)}")
print(f"Max: {np.max(arr)}")
print(f"Mean: {np.mean(arr)}")
print(f"Sum: {np.sum(arr)}")

# 2. Replace values > 30 with 999 using np.where()
# Syntax: np.where(condition, value_if_true, value_if_false)
replaced_arr = np.where(arr > 30, 999, arr)
print(f"Replaced array: {replaced_arr}")

# 3. Limit values between 15 and 45 using np.clip()
clipped_arr = np.clip(arr, 15, 45)
print(f"Clipped array: {clipped_arr}")
