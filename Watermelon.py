def can_divide_watermelon(w):
    if w % 2 == 0 and w >= 4:
        return "YES"
    else:
        return "NO"

# Example usage:
w = int(input())
print(can_divide_watermelon(w))
