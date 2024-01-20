import random

def binary_search(arr, x):
    iter_count = 0
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
        iter_count += 1
        
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return (iter_count, x)
 
    # якщо елемент не знайдений
    try:
        return (iter_count, arr[high+1])
    except:
        return (iter_count, None)


if __name__ == "__main__":
    numbers = sorted([round(random.random()*10, 2) for _ in range(20)])
    print(numbers)
    print(binary_search(numbers, 5))
