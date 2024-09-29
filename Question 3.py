#Altruisty Coding Challenge

print("Question no 3\n")
def max_of_min_subarrays(arr, k):
    n = len(arr)
    min_values = []

    for i in range(n - k + 1):
        min_values.append(min(arr[i:i + k]))

    return max(min_values)

k = 1
arr = [1, 2, 3, 1, 2]
print(max_of_min_subarrays(arr, k)) 
