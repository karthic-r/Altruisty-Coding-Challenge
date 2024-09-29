#Altruisty Coding Challenge

print("Question no 4\n")
def find_odd_balloon_color(n, balloons):
    color_count = {}

    for color in balloons:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    for color in balloons:
        if color_count[color] % 2 != 0:
            return color

    return "All are even"

n = 7
balloons = ['r', 'g', 'b', 'b', 'g', 'y', 'y']
print(find_odd_balloon_color(n, balloons))  

n = 10
balloons = ['a', 'b', 'b', 'b', 'c', 'c', 'c', 'a', 'f', 'c']
print(find_odd_balloon_color(n, balloons))  
