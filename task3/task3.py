import json

with open('task3/tests.json', 'r') as file:
    tests_data = json.load(file)

with open('task3/values.json', 'r') as file:
    values_data = json.load(file)

def update_tests(tests, values):
    for test in tests:
        for value in values:
            if value['id'] == test['id']:
                test['value'] = value['value']
        if 'values' in test:
            update_tests(test['values'], values)

update_tests(tests_data['tests'], values_data['values'])

with open('report.json', 'w') as file:
    json.dump(tests_data, file, indent=4)
