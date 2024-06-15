import json


def employees_rewrite(sort_type):
    if sort_type not in ['firstName', 'lastName', 'department', 'salary']:
        raise ValueError('Bad key for sorting')

    with open('employees-test.json', 'r') as json_file:
        json_data = json.load(json_file)
        employees = json_data['employees']

    if sort_type == 'firstName':
        sort_key = lambda x: x[sort_type].lower()
    elif sort_type == 'lastName':
        sort_key = lambda x: x[sort_type].lower()
    elif sort_type == 'department':
        sort_key = lambda x: x[sort_type].lower()
    else:
        sort_key = lambda x: int(x[sort_type])

    sorted_employees = sorted(employees, key=sort_key)

    with open(f'employees_{sort_type}_sorted.json', 'w') as file:
        json.dump({'employees': sorted_employees}, file, indent=2)


# Пример использования
employees_rewrite('lastName')
# employees_rewrite("firstName")
# employees_rewrite("department")
# employees_rewrite("salary")











# ЧЕРНОВИК


# def employees_rewrite(sort_type):
#     if sort_type not in ['firstName', 'lastName', 'department', 'salary']:
#         raise ValueError('Нет такого ключа')
#
#     with open('employees-test.json', 'r') as json_file:
#         json_data = json.load(json_file)
#
#         # l = json.loads(json_data)
#         # sorted(json_data, key=lambda x: x['salary'])
#     #
#     employees = json_data['employees']
#     # sorted_employees = sorted(employees,
#     #                           key=lambda x: int(x[sort_type]) if x[sort_type].isdigit() else x[sort_type])
#     sorted_employees = sorted(employees, key=lambda x: int(x[sort_type]) if x[sort_type].isdigit() else x[sort_type])
#
# # Сортировка по фамилии:
#     with open(f'employees_sorted_lastName.json', 'w') as file:
#         json.dump({'employees': sorted_employees}, file, indent=2)
# #Сортировка по имени:
#     with open(f'employees_sorted_firstName.json', 'w') as file:
#         json.dump({'employees': sorted_employees}, file, indent=2)
#
# #Сортировка по отделам:
#     with open(f'employees_sorted_department.json', 'w') as file:
#         json.dump({'employees': sorted_employees}, file, indent=2)
#
# #Сортировка по зп:
#     # with open(f'employees_sorted_salary.json', 'w') as file:
#     #     json.dump({'employees': sorted_employees}, file, indent=2)
#
#
# employees_rewrite("lastName")
# # employees_rewrite("firstName")
# # employees_rewrite("department")
# # employees_rewrite("salary")







# with open('employees-test.json', 'r') as json_file:
#     json_data = json.load(json_file)