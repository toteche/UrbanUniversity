first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Задача 1
first_result = [s for s in first_strings if len(s) >= 5]
print("First Result:", first_result)

# Задача 2
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]
print("Second Result:", second_result)

# Задача 3
combined_strings = first_strings + second_strings
third_result = {s: len(s) for s in combined_strings if len(s) % 2 == 0}
print("Third Result:", third_result)