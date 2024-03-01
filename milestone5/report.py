import csv
import argparse
from collections import defaultdict
from datetime import datetime


def filter_by_month(records, month, date_field):
    month_num = datetime.strptime(month, '%B').month
    filtered = [record for record in records if
                datetime.strptime(record[date_field], '%Y-%m-%d').month ==
                month_num]
    return filtered


def generate_report(database_filename, month, verbose):
    with open(database_filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        birthdays = filter_by_month(reader, month, 'Birthdate')
        file.seek(0)
        next(reader)
        anniversaries = filter_by_month(reader, month, 'Hiring Date')

        birthday_report = defaultdict(list)
        for record in birthdays:
            birthday_report[record['Department']].append(record['Name'])
        
        anniversary_report = defaultdict(list)
        for record in anniversaries:
            anniversary_report[record['Department']].append(record['Name'])

        print(f'Report for {month} generated')
        print('---Birthdays---')
        print(f'Total Birthdays: {sum([len(names) for names in
                                       birthday_report.values()])}')
        print('By department:')
        for department, names in birthday_report.items():
            print(f'- {department}: {len(names)}')
            if verbose:
                for name in names:
                    print(name)
        print('---Anniversaries---')
        print(f'Total Anniversaries: {sum([len(names) for names in
                                      anniversary_report.values()])}')
        print('By department:')
        for department, names in anniversary_report.items():
            print(f'- {department}: {len(names)}')
            if verbose:
                for name in names:
                    print(name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a report based on birthdays and hiring dates.')
    parser.add_argument('database_filename', type=str, help='The database file name')
    parser.add_argument('month', type=str, help='The month for the report')
    parser.add_argument('-v', '--verbose', action='store_true', help='Include employee names in the report')

    args = parser.parse_args()

    generate_report(args.database_filename, args.month, args.verbose)
