def is_qualified(score, threshold):
    return score >= threshold


# Test cases
print(is_qualified(90, 85))
print(is_qualified(80, 85))
print(is_qualified(85, 85))