import random

def cypher_code():
    if max_result == 3:
        return "12"
    if max_result == 4:
        return "13"
    if max_result == 5:
        return "14,23"
    if max_result == 6:
        return "12,15,24"
    if max_result == 7:
        return "16,25,34"
    if max_result == 8:
        return "13,17,26,35"
    if max_result == 9:
        return "12,18,27,36,45"
    if max_result == 10:
        return "14,19,23,28,37,46"
    if max_result == 11:
        return "29,38,47,56"
    if max_result == 12:
        return "12,13,15,11,42,39,48,57"
    if max_result == 13:
        return "11_2,2_11,3_10,49,58,67"
    if max_result == 14:
        return "16,11_3,25,2_12,34,3_11,4_10,59,68"
    if max_result == 15:
        return "12,14,1_14,23,2_13,3_12,4_11,5_10,69,78"
    if max_result == 16:
        return "13,17,1_15,26,2_14,35,3_13,4_12,5_11,6_10,79"
    if max_result == 17:
        return "11_6,2_15,3_14,4_13,5_12,6_11,7_10,89"
    if max_result == 18:
        return "12,15,18,11_7,24,27,2_16,36,3_15,45,4_14,5_13,6_12,7_11,810"
    if max_result == 19:
        return "11_8,2_17,3_16,4_15,5_14,6_13,7_12,8_11,910"
    if max_result == 20:
        return "13,14,19,11_9,23,28,2_18,37,3_17,46,4_16,5_15,6_14,7_13,8_12,9_11"


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
current_results = []

cypher = random.randint(3, 20)
print(f'{cypher}')

for digit in digits:
    if cypher % digit == 0:
        # print(f"{digit}")
        current_results.append(digit)
        # print(f'{current_results}')

max_result = max(current_results)
# print(f"Max = : {max_result}")
print(f"Пары чисел выбранные: {cypher_code()}")