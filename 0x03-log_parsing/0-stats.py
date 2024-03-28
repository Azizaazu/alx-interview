#!/usr/bin/python3

import sys
import re

# Define regular expression pattern to match input format
pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$')

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    # Read input from stdin line by line
    for line in sys.stdin:
        line = line.strip()
        match = pattern.match(line)
        if match:
            # Extract relevant information from the line
            ip_address, date, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)

            # Update metrics
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1

            # Check if 10 lines have been processed
            if line_count % 10 == 0:
                # Print statistics
                print("Total file size:", total_file_size)
                for code, count in sorted(status_code_counts.items()):
                    if count > 0:
                        print("{}: {}".format(code, count))

        # Check for keyboard interruption
        if line_count % 10 == 0:
            try:
                sys.stdin.flush()
            except KeyboardInterrupt:
                print("\nKeyboard interruption detected.")
                print("Total file size:", total_file_size)
                for code, count in sorted(status_code_counts.items()):
                    if count > 0:
                        print("{}: {}".format(code, count))
                sys.exit(0)

except KeyboardInterrupt:
    print("\nKeyboard interruption detected.")
    print("Total file size:", total_file_size)
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))
    sys.exit(0)
