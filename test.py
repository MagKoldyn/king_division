import matplotlib.pyplot as plt
from main import calc
import numpy as np
import time
fact_steps_list = []
want_steps_list = []
diff_list = []
approximated_list = []
fact_app_diff_list = []
steps_number = range(3,203,2)
for n in steps_number:
    start_coin_list = [0] * (n - 1) + [3*n]
    fact_steps = calc(start_coin_list, 100000)
    fact_steps_list.append(fact_steps)
    want_steps = (((n - 3) + 2) / 2) * ((n - 3) / 2) + 3
    want_steps_list.append(want_steps)
    if fact_steps != want_steps:
        print(f'n = {n}, fact_steps = {fact_steps}, want_steps = {want_steps}. ')
# print(calc([0,0,15,0,0], 10))
for i in range(len(fact_steps_list)):
    diff_list.append(int(want_steps_list[i] - fact_steps_list[i]))
print(diff_list)

for i in steps_number:
    approximated_list.append(0.20 * i ** 2 - 0.03 * i - 0.51)

for i in range(len(fact_steps_list)):
    fact_app_diff_list.append(int(approximated_list[i] - fact_steps_list[i]))
plt.plot(steps_number, fact_steps_list)
plt.plot(steps_number, want_steps_list)
plt.plot(steps_number, diff_list)
# plt.plot(steps_number, approximated_list)
# plt.plot(steps_number, fact_app_diff_list)
plt.show()
print(list(steps_number))
print(fact_steps_list)
print(fact_app_diff_list)
print(0.20 * 1001 ** 2 - 0.03 * 1001 - 0.51)
a = '3, 5, 9, 15, 23, 33, 45, 59, 73, 89, 107, 125, 147, 171, 195, 221, 249, 277, 309, 341, 375, 411, 449, 487, 529, 571, 615, 661, 707, 755, 807, 857, 913, 969, 1025, 1085, 1145, 1207, 1271, 1333, 1403, 1471, 1539, 1611, 1685, 1759, 1837, 1915, 1995, 2079, 2159, 2245, 2333, 2419, 2509, 2601, 2693, 2789, 2885, 2981, 3083, 3185, 3285, 3391, 3495, 3605, 3713, 3823, 3935, 4051, 4165, 4283, 4403, 4523, 4647, 4769, 4895, 5023, 5149, 5281, 5413, 5545, 5683, 5819, 5957, 6097, 6241, 6383, 6531, 6675, 6825, 6975, 7123, 7281, 7433, 7591, 7747, 7909, 8071'
a = a.replace(',', '')
print(a)