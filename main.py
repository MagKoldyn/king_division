import time


def calc(start_coin_list, iterations):
    list_len = len(start_coin_list)
    current_values = start_coin_list.copy()
    for j in range(iterations):
        new_list_appenders = [0] * list_len
        new_list_values = [0] * list_len
        for i in range(list_len):
            if i + 1 == list_len:
                new_list_appenders[i - 1] += current_values[i] // 2
                new_list_appenders[0] += current_values[i] // 2
                if current_values[i] % 2 == 0:
                    new_list_values[i] = 0
                else:
                    new_list_values[i] = 1
            else:
                new_list_appenders[i - 1] += current_values[i] // 2
                new_list_appenders[i + 1] += current_values[i] // 2
                if current_values[i] % 2 == 0:
                    new_list_values[i] = 0
                else:
                    new_list_values[i] = 1

        for i in range(list_len):
            current_values[i] = new_list_values[i] + new_list_appenders[i]

        # print(current_values)

        if set(current_values) == {3}:
            print(j + 1)
            return j + 1
