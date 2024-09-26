import random

def generate_random_numbers():
    return [random.randint(0, 1000) for _ in range(100)]

def merge_sort(arr):
    # Base case: if the list is a single element, return it
    if len(arr) <= 1:
        return arr

    # Finding the middle index of the array
    mid = len(arr) // 2

    # Recursively split and sort both halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merging both halves
    return merge(left_half, right_half)


# Function to merge two sorted lists
def merge(left, right):
    sorted_list = []
    left_index = right_index = 0

    # Merge the two lists while maintaining order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    # If there are remaining elements in the left list, add them
    sorted_list.extend(left[left_index:])

    # If there are remaining elements in the right list, add them
    sorted_list.extend(right[right_index:])

    return sorted_list



def calculate_averages(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]

    even_avg = sum(evens) / len(evens) if evens else 0
    odd_avg = sum(odds) / len(odds) if odds else 0

    return even_avg, odd_avg


if __name__ == "__main__":
    #Generate a list of 100 random numbers
    random_numbers = generate_random_numbers()

    # Sort the list using merge sort
    sorted_numbers = merge_sort(random_numbers)

    #Calculate the average for even and odd numbers
    even_avg, odd_avg = calculate_averages(sorted_numbers)

    #Print the average for even and odd numbers
    print(f"Average of even numbers: {even_avg}")
    print(f"Average of odd numbers: {odd_avg}")
    print(sorted_numbers)