calls = 0

def count_calls(func):
    global calls
    def wrapper (*args, **kwargs):
        global calls
        calls += 1
        return func(*args, **kwargs)
    return wrapper

@count_calls
def string_info(string):
    return len(string), string.upper(), string.lower()

@count_calls
def is_contains(string, list_to_search):
    string = string.lower()
    lower_list = [s.lower() for s in list_to_search]
    return string in lower_list

string = string_info('Capybara')
print(string)

string = string_info('Armageddon')
print(string)

print(is_contains("Urban", ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(f'Количество выполнений: {calls}')


