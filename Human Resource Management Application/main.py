# This entire application was created by Mohamed Riham from CSD21 Batch.
# ID = 1028401
from authentication import authenticate
from hrm import Employee

user = Employee("1028401", "Mohamed Riham", "Manager", "HR", "2024-01-04", "Active")


def main():
    employees = Employee.Load_Employees()
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if authenticate(username, password):
            print("Authentication successful.\n")
            print()
            print("Main Menu:")
            print("1. View Personal Information")
            print("2. View All Employee Information")
            print("3. Search Employee by ID")
            print("4. Add New Employee")
            print("5. Remove Employee")
            print("6. Update Personal Information")
            print("7. Submit Leave Request")
            print("8. View Company Policies")
            print("9. Access Work Schedules")
            print("10. Exit")
            print()
            while True:
                choice = input("Enter your choice: ")

                if choice == "1":
                    print()
                    print(user.__view_personal_info__())

                elif choice == "2":
                    print()
                    Employee.view_employees()

                elif choice == "3":
                    print()
                    emp_id = input("Enter the employee ID to search for: ")
                    found_employee = Employee.search_employee_by_id(emp_id)
                    if found_employee:
                        print("Employee found:")
                        print(
                            f"ID: {found_employee.emp_id}, Name: {found_employee.name}, Position: {found_employee.position}, Department: {found_employee.department}, Hire Date: {found_employee.hire_date}, Status: {found_employee.employment_status}")
                    else:
                        print("No employee found with the given ID.")

                elif choice == "4":
                    print()
                    user.add_employee(employees)
                    user.save_employees(employees)

                elif choice == "5":
                    print()
                    user.remove_employee(employees)

                elif choice == "6":
                    print()
                    new_position = input("Enter new position: ")
                    new_department = input("Enter new department: ")
                    update_sts = user.__update_personal_info__(new_position, new_department)
                    print(update_sts)

                elif choice == "7":
                    Employee.__submit_leave_request__()

                elif choice == "8":
                    print()
                    policies = user.__view_company_policies__()
                    print(policies.read())
                    print()

                elif choice == "9":
                    print()
                    schedules = user.__access_work_schedules__()
                    print(schedules.read())
                    print()

                elif choice == "10":
                    exit_function = input('Do you want to exit?(yes / no): ')
                    if exit_function == 'no':
                        print('logging Out....')
                        print()
                        break
                    elif exit_function == 'yes':
                        print('Exiting from the session...')
                        exit()
                    else:
                        print('invalid input. Please try again......')

                else:
                    print("Invalid choice. Please try again...")

        else:
            print("Authentication failed. Please try again...\n")


if __name__ == "__main__":
    main()
