#!/usr/bin/python
import subprocess

temp_info = subprocess.check_output("sensors")

temp_info = temp_info.decode('utf-8')

temp = temp_info.split('\n')

i_index = temp[2].index('+')
f_index = temp[2].index('C')

temp1 = temp[2][i_index+1:f_index]
temp2 = temp[3][i_index+1:f_index]


print(f"core1: {temp1} | core2: {temp2}")
