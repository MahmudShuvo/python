def twoSum(nums, target):
    # Iterate through each element in the list
    for i in range(len(nums)):
        # For each element, iterate through the rest of the list
        for j in range(i + 1, len(nums)):
            # If the sum of the two elements equals the target, return their indices
            if nums[i] + nums[j] == target:
                return [i, j]

# Taking input from the user
nums = list(map(int, input("Enter the numbers (space-separated): ").split()))
target = int(input("Enter the target: "))

# Calling the twoSum function and printing the result
result = twoSum(nums, target)
if result:
    print(f"The indices of the two numbers that add up to the target are: {result}")
else:
    print("No solution found")
