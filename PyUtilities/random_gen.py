import random
import os

def shuffle(string):
    temp_list = list(string)
    random.shuffle(temp_list)
    return ''.join(temp_list)


def random_password(n_upper, n_lower, n_digit, n_symbol, n_shuffle):
    upper_chars = []
    lower_chars = []
    digits = []
    symbols = []

    for u in range(n_upper):
        t_uppercase_letter = chr(random.randint(65, 90))
        upper_chars.append(t_uppercase_letter)

    for l in range(n_lower):
        t_lowercase_letter = chr(random.randint(97, 122))
        lower_chars.append(t_lowercase_letter)

    for d in range(n_digit):
        t_digit = chr(random.randint(48, 57))
        digits.append(t_digit)

    for s in range(n_symbol):
        t_symbol = chr(random.randint(33, 47))
        symbols.append(t_symbol)

    #print(f"{upper_chars} upper")
    #print(f"{lower_chars} lower")
    #print(f"{digits} digits")
    #print(f"{symbols} symbols")

    upper_char_string = ''.join(upper_chars)
    lower_char_string = ''.join(lower_chars)
    digit_string = ''.join(digits)
    symbols_string = ''.join(symbols)

    initial_gen = (upper_char_string + lower_char_string +
                   digit_string + symbols_string)
    temp_string = initial_gen
    os.system('cls')
    print(f"Initial: {initial_gen}")

    for n in range(n_shuffle):
        next_shuffle = shuffle(temp_string)
        temp_string = next_shuffle
        print(f"Shuffle {n + 1}: {next_shuffle}")



random_password(2, 2, 4, 3, 4)