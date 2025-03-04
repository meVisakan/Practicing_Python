# Q- You are given a 1-indexed array of length N, where each element represents a bag containing that many balls.
# If a bag is at an odd index, you can only retrieve a prime number of balls from it.
# If a bag is at an even index, you can only retrieve a non-prime number of balls from it.
# Your task is to calculate the total number of unique ways to retrieve balls from all the bags.

def is_prime(n):
    """Returns True if n is a prime number, otherwise False."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def get_valid_selections(n, is_odd_index):
    """Returns the count of valid ways to pick balls from a bag."""
    valid_count = 0
    for i in range(2, n + 1):
        if (is_odd_index and is_prime(i)) or (not is_odd_index and not is_prime(i)):
            valid_count += 1
    return valid_count


def total_combinations(arr):
    """Calculates total valid ball selection combinations."""
    total_ways = 1
    for i in range(len(arr)):
        bag_size = arr[i]
        is_odd_index = (i + 1) % 2 == 1  # 1-based index check
        ways = get_valid_selections(bag_size, is_odd_index)
        total_ways *= max(ways, 1)  # Ensure at least 1 way
    return total_ways


# Example usage
arr = [3, 5, 9, 11]
print(total_combinations(arr))  # Output: 40
