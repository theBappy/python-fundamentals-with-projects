# List Comprehension = A concise way to create lists in Python, compact and easier to read than traditional loops [expression for value in iterable if condition]

# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)
# print(doubles)

'''doubles = [expression for value in iterable if condition]'''
# doubles = [x * 2 for x in range(1, 11)]
# print(doubles)

# cubes = [x ** 3 for x in range(1, 11)]
# print(cubes)

# triples = [ y * 3 for y in range(1,11)]
# print(triples)

# squared = [z * z for z in range(1, 11)]
# print(squared)

# fruits = ["apple", "orange", "banana","coconut"]
# fruits = [fruit.upper() for fruit in fruits]
# fruits = [fruit.upper() for fruit in fruits]
# fruits = [fruit.upper() for fruit in ["apple", "orange", "banana","coconut"]]
# fruit_chars = [fruit[0].upper() for fruit in fruits]
# print(fruit_chars)

# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0 and num != -4]
# print(negative_nums)
# numbers = [1, -2, 3, -4, 5, -6, 8]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2]
# print(odd_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)



