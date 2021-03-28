#!/usr/bin/python
import os

op    = os.popen(r'pactl list sinks | grep -e "Volume" -e "Mute"').read()

# removes tabulation and splits volume and mute status
op    = op.strip('\t').rsplit('\n')

muted = op[0].strip('Mute: ')
if muted == 'yes':
    muted = "Mute | "
else:
    muted = ''

# filter volume output
vol   = op[1].strip('Volume: ').replace(' ','').rsplit(',')
left  = vol[0].rsplit('/')[1]
right = vol[1].rsplit('/')[1]

print(f'{muted}left: {left} | right: {right}')
