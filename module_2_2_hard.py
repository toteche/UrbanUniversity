import random

digit = random.randint(3, 20)

pairs = []
summs = []
generated_result = []

for i in range(1, 20):
    for j in range(i + 1, 21):
        pair = (i, j)
        sum = i + j
        pairs.append(pair)
        summs.append(sum)

    for index, sum in enumerate(summs):
        if digit % sum == 0:
            generated_result.append((digit, pairs[index]))

unique_pairs = list(set(generated_result))
sorted_pairs = sorted(unique_pairs, key=lambda x: x[1])


formatted_pairs = [item[1] for item in sorted_pairs]

print(f"{digit} | {', '.join(map(str, formatted_pairs))}")