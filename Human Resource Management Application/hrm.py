# This entire application was created by Mohamed Riham from CSD21 Batch.
# ID = 1028401
class Employee:
    Employees_Data = "Files/employees_data.txt"

    def __init__(self, emp_id, name, position, department, hire_date, employment_status):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.department = department
        self.hire_date = hire_date
        self.employment_status = employment_status

    def __view_personal_info__(self):
        return f"ID: {self.emp_id}\nName: {self.name}\nPosition: {self.position}\nDepartment: {self.department}\nHire Date: {self.hire_date}\nStatus: {self.employment_status}"

    def __update_personal_info__(self, new_position, new_department):
        self.position = new_position
        self.department = new_department
        return "personal information updated successfully...."

    @classmethod
    def view_employees(cls):
        try:
            with open(cls.Employees_Data, "r") as file:
                print("Employee Details:")
                for line in file:
                    emp_id, emp_name, emp_position, emp_department, emp_hire_date, employment_status = line.strip().split(",")
                    print(f"Employee ID: {emp_id}")
                    print(f"Name: {emp_name}")
                    print(f"Position: {emp_position}")
                    print(f"Department: {emp_department}")
                    print(f"Hire Date: {emp_hire_date}")
                    print(f"Employment Status: {employment_status}")
                    print()
        except FileNotFoundError:
            print("Employees data file not found...")

    @classmethod
    def Load_Employees(cls, employees=None):
        if employees is None:
            employees = []
        try:
            with open(cls.Employees_Data, "r") as file:
                for line in file:
                    emp_id, emp_name, position, department, hire_date, status = line.strip().split(",")
                    employees.append(Employee(emp_id, emp_name, position, department, hire_date, status))
            return employees
        except FileNotFoundError:
            print("Employees data File Not Found...")

    def save_employees(self, employees):
        with open(self.Employees_Data, "w") as file:
            for employee in employees:
                file.write(
                    f"{employee.emp_id},{employee.name},{employee.position},{employee.department},{employee.hire_date},{employee.employment_status}\n")

    @staticmethod
    def search_employee_by_id(emp_id):
        try:
            with open(Employee.Employees_Data, "r") as file:
                for line in file:
                    emp_details = line.strip().split(",")
                    if emp_details[0] == emp_id:
                        return Employee(*emp_details)
            return None
        except FileNotFoundError:
            print("Employees data File Not Found...")

    def add_employee(self, employees):
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        position = input("Enter employee position: ")
        department = input("Enter employee department: ")
        hire_date = input("Enter employee hire date (YYYY-MM-DD): ")
        status = input("Enter employee status: ")
        new_employee = Employee(emp_id, name, position, department, hire_date, status)
        employees.append(new_employee)
        self.save_employees(employees)
        print("Employee added successfully....")

    def remove_employee(self, employees):
        emp_id = input("Enter employee ID to remove: ")
        for employee in employees:
            if employee.emp_id == emp_id:
                employees.remove(employee)
                self.save_employees(employees)
                print("Employee removed successfully...")
                return
        print("Employee not found...")

    @staticmethod
    def __submit_leave_request__():
        leave_type = input("Leave type: ")
        duration = input("Duration: ")
        details = input("More Details about leave: ")
        hehe = "Successfully added leave request...."
        print(hehe)
        return leave_type, duration, details

    @staticmethod
    def __view_company_policies__():
        policies = open("Files/Company Policies.txt", "r")
        return policies

    @staticmethod
    def __access_work_schedules__():
        schedules = open("Files/Work Schedule.txt", "r")
        return schedules
