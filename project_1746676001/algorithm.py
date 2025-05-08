# Linear Search Implementation
# A simple search algorithm that scans each element in a list.

def linear_search(arr, target):
    """Search for a target value in an array using linear search."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    # Test linear search
    arr = [38, 27, 43, 3, 9, 82, 10]
    print(f"Array: {arr}")
    
    target = 43
    result = linear_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in array")
