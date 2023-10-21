from main import calc
import time

for n in range(3,102,2):
    start_coin_list = [0] * (n - 1) + [3*n]
    fact_steps = calc(start_coin_list, 2450)
    want_steps = (((n - 3) + 2) / 2) * ((n - 3) / 2) + 3
    if fact_steps != want_steps:
        print(f'n = {n}, fact_steps = {fact_steps}, want_steps = {want_steps}. ')
# print(calc([0,0,15,0,0], 10))
