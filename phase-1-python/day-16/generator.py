import sys
""""
list_comp=[x**2 for x in range(1000000)]
print(sys.getsizeof(list_comp))

gen_exp=(x**2 for x in range(1000000))
print(sys.getsizeof(gen_exp))

dict_comp={x: x**2 for x in range(1000000)}
print(sys.getsizeof(dict_comp))"""

my_gen=(n for n in range(3))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))  # This will raise StopIteration since the generator is exhausted