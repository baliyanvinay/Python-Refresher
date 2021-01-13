# Transpose a square matrix of n by n


# Write a function that will place even elements at even locations and odd at odd locations
def even_odd_locations(input_array):
    '''
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


sample_input = [1, 2, 3, 4, 5, 6]
sample_output = even_odd_locations(sample_input)
print(sample_output)
