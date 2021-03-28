#!/usr/bin/python
import os 

output = os.popen(r'free -h')

mem = output.read()

tmp = mem.split('\n')

memory = tmp[1].split(' ')

memory = [i for i in memory if i != '']
print(f"Mem: {memory[2]}/{memory[1]}")

