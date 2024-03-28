#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""


import sys


status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_file_size = 0
line_count = 0


try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        if len(parts) != 7:
            continue

        try:
            file_size = int(parts[5])
            status_code = int(parts[3])
        except ValueError:
            continue

        total_file_size += file_size
        line_count += 1

        if status_code in status_counts:
            status_counts[status_code] += 1

        if line_count % 10 == 0:
            print_statistics()

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_file_size))
    for key, value in sorted(status_counts.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
