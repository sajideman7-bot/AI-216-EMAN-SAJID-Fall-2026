from score_utils import calculate_average, is_passing, count_above_threshold


scores = [72, 88, 45, 91, 67]

average = calculate_average(scores)
passing = is_passing(scores[0])
above_80 = count_above_threshold(scores, 80)

print("Average:", average)
print("First score is passing:", passing)
print("Scores at least 80:", above_80)