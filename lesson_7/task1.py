import csv
from datetime import date

exchange_rate = 27.5

input_file = 'test_file.csv'
output_file = 'salaries_uah.csv'

with open(input_file, 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    rows = list(reader)

    salary_start_index = headers.index('Jan')
    salary_end_index = headers.index('Dec')

    for row in rows:
        salaries_usd = [float(row[i]) for i in range(salary_start_index, salary_end_index + 1)]
        salaries_uah = [salary_usd * exchange_rate for salary_usd in salaries_usd]
        for i in range(salary_start_index, salary_end_index + 1):
            row[i] = salaries_uah[i - salary_start_index]

headers.extend(['Date'])
current_date = date.today().strftime('%Y-%m-%d')

for row in rows:
    row.extend([current_date])

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)
