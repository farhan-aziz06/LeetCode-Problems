def find_element(array, target):
    for i in range (0, len(array)):
        for j in range (i+1, len(array)):
            add = array[i] + array [j]
            if (add == target):
                return array[i], array[j]
            
array = [2,3,4,5,6]
target = 10;
result = find_element(array, target)
print(result)