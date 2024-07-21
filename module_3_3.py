def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(3, "hello", False)
print_params(4, 56)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [22, "sun", 4.5]
values_dict = {'a': 92, 'b': "rain", 'c': 3.5}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [356, "bye"]
print_params(*values_list_2, 42)
