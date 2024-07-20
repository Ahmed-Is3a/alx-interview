#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''

import sys
import signal

# Initialize variables
status_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                 '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
line_counter = 0


def print_statistics():
    '''Prints the current statistics'''
    print('File size: {}'.format(total_file_size))
    for status_code, count in sorted(status_counts.items()):
        if count != 0:
            print('{}: {}'.format(status_code, count))


def signal_handler(sig, frame):
    '''Handles the SIGINT signal (Ctrl+C)'''
    print_statistics()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)


# Process each line from stdin
for line in sys.stdin:
    line_parts = line.split(" ")
    if len(line_parts) > 4:
        try:
            status_code = line_parts[-2]
            file_size = int(line_parts[-1])
            if status_code in status_counts.keys():
                status_counts[status_code] += 1
            total_file_size += file_size
            line_counter += 1

            if line_counter == 10:
                line_counter = 0
                print_statistics()

        except ValueError:
            # Skip lines with invalid size values
            continue

# Print final statistics
print_statistics()
