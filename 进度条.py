import time
from rich.progress import track
from tqdm import trange
import os

pass  # 进度条time模块配合\r
# for R_time in range(10):
#     print(i_num, end="\r")
#     print()
#     # print("\r", end='')
#     # print('Time Remaining: %d' % R_time, end='', flush=True)
#     time.sleep(1)

for i in range(1, 20):
    print("█" * i + "%*.*s" % (42 - 2 * i, 5, int(i * 100 / 19)) + "%", end='\r')
    time.sleep(1)
print("\n")

pass  # 进度条rich模块
# for step in track(range(30)):
#     print('早起Python')
#     time.sleep(0.5)
pass  # 进度条tqdm模块
# for i in trange(123):
#     print("print function")
#     time.sleep(0.1)
