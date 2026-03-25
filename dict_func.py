def employee_print(employee_info):
    extra_info = employee_info.copy()

    print(f"Name: {extra_info.pop('Name', 'N/A')}")
    print(f"Salary: {extra_info.pop('Salary', 'N/A')}")
    print(f"Role: {extra_info.pop('Role', 'N/A')}")

    if extra_info:
        for key, value in extra_info.items():
            print(f"{key}: {value}")
    else:
        print("No other info!")
