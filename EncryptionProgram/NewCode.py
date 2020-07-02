import csv
import time
from vigenerecipher import encode
from datetime import datetime
from part_of_day import get_part_of_day

key = input('Enter key: ')

# Weekday Dictionary
weekday_dict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

with open('sample_input.csv', 'r') as csv_file:
    '''
    Opens file to read
    '''
    with open('sample_output.csv', 'w', newline='') as new_file:
        '''
        Opens new file to write
        '''
        csv_writer = csv.writer(new_file)

        # Add the new columns onto the header

        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)
        headings.append('part_of_day')
        headings.append('ISO date')
        headings.append('day_of_week')

        # Determine index for email and timestamp
        email_index = headings.index('email')
        timestamp_index = headings.index('timestamp')

        csv_writer.writerow(headings)

        for line in csv_reader:
            # ---- Encrypting emails ----

            # Splits emails into username and domain
            email_address = line[email_index]
            email_components = (email_address.split('@'))

            username = email_components[0]
            domain = email_components[1]

            # Encrypts the emails and mutates the email value of the line
            encrypted_username = encode(key, username)
            encrypted_email = '{0}@{1}'.format(encrypted_username, domain)

            line[email_index] = encrypted_email

            # Converting timestamps into datetime object
            ts = line[timestamp_index]
            ts_as_dt = datetime.fromtimestamp(int(ts))

            # ---- Part of day ----
            hour_value = ts_as_dt.hour
            part_of_day = get_part_of_day(hour_value)
            line.append(part_of_day)

            # ---- ISO Date ----
            iso_str = ts_as_dt.isoformat()
            line.append(iso_str)

            # ---- Day of Week ----
            day_of_week = weekday_dict[ts_as_dt.weekday()]
            line.append(day_of_week)

            # Writes to file
            csv_writer.writerow(line)