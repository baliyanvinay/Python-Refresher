def transpose_matrix(input_matrix):
    '''
    Row element turns into column element
    '''
    n = len(input_matrix)
    for i in range(n):
        for j in range(i):  # this has to only till i
            input_matrix[i][j], input_matrix[j][i] = input_matrix[j][i], input_matrix[i][j]
    return input_matrix


def even_odd_locations(input_array):
    '''
    Write a function that will place even elements at even locations and odd at odd locations
    '''
    even_array, odd_array = [], []
    for element in input_array:
        if element % 2 == 0:
            even_array.append(element)
        else:
            odd_array.append(element)
    # checking which array has more elements
    len_loop = len(input_array)//2
    # output array
    output_array = []
    for _ in range(len_loop):
        output_array.extend([even_array.pop(0), odd_array.pop(0)])
    return output_array


def isValidSubsequence(array, sequence):
    for element in sequence:
        if element not in array:
            return False
    return True


# Transpose a square matrix of n by n
sample_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sample_output = transpose_matrix(sample_matrix)
print('Transpose of matrix : ', *sample_output, sep='\n')  # List unpacking


# Odd Even Element Indexes
sample_input = [1, 2, 3, 4, 5, 6]
sample_output = even_odd_locations(sample_input)
print('Odd Even Element-Index Probelm : ', sample_output)

# Second array valid sequence of first array
first_array = [5, 1, 22, 25, 6, -1, 8, 10]
second_array = [1, 6, -1, 10, 10]
print('Second Array sequence of First Array : ',
      isValidSubsequence(first_array, second_array))
