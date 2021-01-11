# Example of index out of range exception or IndexError

array_list = [1, 2, 3]  # with indexes 0,1,2
try:
    print('In try block: accessing index 3')
    array_list[3] = 12
    array_list[1]/0
except (IndexError, ZeroDivisionError) as exception:
    print('In except block: ', exception)
    array_list.append(12)
else:
    print('In else block: No error')
    array_list.reverse()
finally:
    print('In finally block: Printing list')
    print(array_list)
