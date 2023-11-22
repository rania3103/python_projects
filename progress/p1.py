#!/usr/bin/python3
"""progress line"""
from tqdm import tqdm
from time import sleep
with tqdm (total = 100) as prog:
    for i in range(100):
        sleep(0.1)
        prog.update(1)
print("finish")