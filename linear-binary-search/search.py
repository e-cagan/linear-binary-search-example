array = [13, 2, 55, 23, 11, 66, 8, 99, 4, 1, 6]

def linear_search(target_number):
    for i in range(len(array)):
        if array[i] == target_number:
            print(f"Target number found at index {i}.")
            return
    print(f"Target number {target_number} can't be found in this array.")


def binary_search(target_number):
    while target_number not in array:
        print(f"The number {target_number} not in this array. Please try again.")
        target_number = int(input("Enter a number: "))

    array.sort()
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_number = array[mid]

        if target_number == mid_number:
            print(f"Target number found at index {mid}.")
            return
        elif mid_number < target_number:
            low = mid + 1
        elif mid_number > target_number:
            high = mid - 1

    print(f"Target number {target_number} can't be found in this array.")


# Example usage    
linear_search(23)
binary_search(23)