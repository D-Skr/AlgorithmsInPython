#return min required time required to place mice in holes using the Greedy approach.
#put each mouse to its nearest hole to minimize the time
#this can be done by sorting the positions of mice and holes.


def assign_hole(mice, holes):
    #base - num of mice and holes should be the same
    if len(mice) != len(holes):
        return "Number of mice and holes not same"

    #sorting
    mice.sort()
    holes.sort()

    #finding max difference between mouse and hole
    max_diff = 0

    for i in range(len(mice)):
        if max_diff < abs(mice[i] - holes[i]):
            max_diff = abs(mice[i] - holes[i])

    return max_diff


mice = [4, -4, 2]
holes = [4, 0, 5]

min_time = assign_hole(mice, holes)

print("The last mouse gets into the hole in time: ", min_time)