#!/usr/bin/python3
"""Parse a log file"""

import sys
import re

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

line_count = 0
total_file_size = 0


def print_stats():
    print("File size: {:d}".format(total_file_size))
    for key, value in status_codes.items():
        if value:
            print("{}: {:d}".format(key, value))


log_pattern = (r'^(\d+\.\d+\.\d+\.\d+) - \[(\d{4}-\d{2}-\d{2} '
               r'\d{2}:\d{2}:\d{2}\.\d+)\] "(\w+ [^"]+)" '
               r'([a-zA-Z0-9]+) (\d+)$'
               )

try:
    for line in sys.stdin:
        line_count += 1
        line = line[:-1]
        array = line.split()
        if re.match(log_pattern, line):
            method = str(array[-5][1:])
            status_code = str(array[-2])
            file_size = int(array[-1])
            if method == "GET" and status_code.isnumeric():
                # calc stats
                total_file_size += file_size
                status_codes[status_code] += 1

        if (line_count % 10 == 0):
                    print_stats()
    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
