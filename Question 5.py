#Altruisty Coding Challenge

print("Question no 5\n")
def find_fittest_trainees(oxygen_levels):
    for level in oxygen_levels:
        if level < 1 or level > 100:
            return "INVALID INPUT"

    averages = []
    for i in range(3):
        avg = round(sum(oxygen_levels[i::3]) / 3)
        averages.append(avg)

    max_avg = max(averages)

    if max_avg < 70:
        return "All trainees are unfit"

    fittest_trainees = [i + 1 for i, avg in enumerate(averages) if avg == max_avg]

    result = "\n".join([f"Trainee Number : {trainee}" for trainee in fittest_trainees])
    return result

oxygen_levels = [
    95, 92, 95,  
    92, 90, 92,  
    90, 92, 90  
]

print(find_fittest_trainees(oxygen_levels))
