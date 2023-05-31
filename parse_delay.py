# parse_delay.py
#
# parse a command of this form and
# may also be any of these variations:
#
#  delay 1
#	delay 1.0
#	delay 1s
#	delay 1.0s
#	delay 1000ms
#	delay 1000.0ms
#	delay 1000.0 ms
#	delay 1000000us
#	delay 1000000 us
#	delay 1,000,000us
#	delay 1,000,000 us
#

import re

test_strings = [
    "delay 1",
	"delay 1.0",
	"delay 1s",
	"delay 1.0s",
	"delay 1000ms",
	"delay 1000.0ms",
	"delay 1000.0 ms",
	"delay 1000000us",
	"delay 1000000 us",
	"delay 1,000,000us",
	"delay 1,000,000 us"

        ]

# number part of re:
#delay_re_pattern = r'\w*delay\w+([0-9]+\.?[0-9]*)(\w*)([mu]?s?)'
delay_re_pattern = r'\s*delay\s+([0-9,]+\.?[0-9]*)(\s*)([mu]?)(s?)'

delay_c = re.compile(delay_re_pattern)
if delay_c:
    for test_str in test_strings:
        print(f'test string: {test_str}')
        result = delay_c.match(test_str)
        print(f'result: {result}')
        print(f'result[0] = {result[0]}')
        print(f'result[1] = {result[1]}')
        print(f'result[2] = {result[2]}')
        print(f'result[3] = {result[3]}')
        print(f'result[4] = {result[4]}')

