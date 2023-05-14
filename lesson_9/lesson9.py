import json

with open('group_people.json') as f:
    data = json.load(f)

max_women = 0
group_id = 0

for group in data:
    women_count = 0

    for person in group['people']:
        if person['gender'] == 'Female' and person['year'] > 1977:
            women_count += 1

    if women_count > max_women:
        max_women = women_count
        group_id = group['id_group']

print(f"Identifier of the group with the maximum height of women born after 1977: {group_id}"
      f" Number of women in this group: {max_women}")

import json

with open('manager_sales.json') as file:
    data = json.load(file)

max_sales = 0
best_manager = None

for manager_data in data:
    manager = manager_data['manager']
    sales = sum(car['price'] for car in manager_data['cars'])

    if sales > max_sales:
        max_sales = sales
        best_manager = manager

if best_manager:
    print(f"Most Successful Manager: {best_manager['first_name']} {best_manager['last_name']}"
          f" The total amount of his sales: {max_sales}")
