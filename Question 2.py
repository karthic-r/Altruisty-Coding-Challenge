#Altruisty Coding Challenge

print("Question no 2\n")
def count_frogs_between_stones(s, start_indices, end_indices):
    start_indices = [i - 1 for i in start_indices]
    end_indices = [i - 1 for i in end_indices]

    frog_count = [0] * len(s)
    count = 0
    for i in range(len(s)):
        if s[i] == '*':
            count += 1
        frog_count[i] = count

    results = []
    for start, end in zip(start_indices, end_indices):        
        while start <= end and s[start] != '|':
            start += 1      
        while end >= start and s[end] != '|':
            end -= 1
        if start < end:
            results.append(frog_count[end] - frog_count[start])
        else:
            results.append(0)
    
    return results

s = "*|*|"
start_indices = [1]
end_indices = [3]
results = count_frogs_between_stones(s, start_indices, end_indices)

for result in results:
    print(result)  
