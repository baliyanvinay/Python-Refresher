# List vs Tuple Performance Test
import timeit

# Object Construction Time in Seconds
res = timeit.timeit('(1,2,3,4)')
print('Tuple construction: ', res)
res = timeit.timeit('[1,2,3,4]')
print('List construction: ', res)


# Object Indexing
res = timeit.timeit('for i in (1,2,3,4,5): pass')
print('Tuple Indexing: ', res)
res = timeit.timeit('for i in [1,2,3,4,5]: pass')
print('List Indexing: ', res)
