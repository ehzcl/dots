#!/usr/bin/python
import os

time = os.popen('uptime -p')

time = time.read()

uptime = time[3:].rstrip('\n')

print(f'uptime: {uptime}')
