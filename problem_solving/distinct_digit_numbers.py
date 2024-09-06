

def count_Numbers(arr):
    for x, y in arr:
        counter = 0
        for i in range(x, y+1):
            num = str(i)
            if len(num) == len(set(num)):
                counter += 1
        print(counter)


def count_numbers(arr):
    def has_unique_digits(num):
        num_str = str(num)
        return len(num_str) == len(set(num_str))

    # Generate all numbers with unique digits up to the largest y in arr
    max_y = max(y for _, y in arr)
    unique_digit_numbers = [i for i in range(max_y + 1) if has_unique_digits(i)]

    # Use binary search to quickly find the count of valid numbers within each range
    from bisect import bisect_left, bisect_right

    for x, y in arr:
        left = bisect_left(unique_digit_numbers, x)
        right = bisect_right(unique_digit_numbers, y)
        print(right - left)

# Example usage:
# count_numbers([(1, 20), (9, 19)])



# def conuntNumbers(arr):

def is_unique(n):
    visited = set()

    while n > 0:
        digit = n % 10
        if digit in visited:
            return False
        else:
            visited.add(digit)
        n = n // 10
    return True

print(is_unique(12345))
    