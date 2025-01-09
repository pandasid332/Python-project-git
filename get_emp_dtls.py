import oracledb

def get_employee_details(employee_id):
    """
    Fetch and print employee details for a given employee ID.
    
    :param employee_id: ID of the employee to fetch details for
    :return: None
    """
    # Database connection details
    username = 'scott'
    password = 'tiger'
    dsn = 'localhost:1521/orclpdb'

    try:
        # Establish the connection
        connection = oracledb.connect(user=username, password=password, dsn=dsn)
        cursor = connection.cursor()

        # Query to get employee details
        query = "select e.empno,e.ename emp_name,e.job,coalesce(e1.ename,'He is the CEO') mgr_name,e.hiredate,e.sal from emp e join emp e1 on e.mgr=e1.empno(+) where e.empno = :emp_id"
        cursor.execute(query, emp_id=employee_id)

        # Fetch the employee details
        employee_details = cursor.fetchone()
        
        if employee_details:
            print("Employee Details:")
            print("*******************************************")
            print()
            print("Employee ID:", employee_details[0])
            print("Employee Name:", employee_details[1])
            print("Employee job:", employee_details[2])
            print("Employee manager:", employee_details[3])
            print("Hire Date:", employee_details[4])
            print("Employee salary:", employee_details[5])
            print()
            print("*******************************************")
        else:
            print("No employee found with ID:", employee_id)
        
        # Close the cursor and connection
        cursor.close()
        connection.close()
    except oracledb.DatabaseError as e:
        print("There was a problem connecting to the database:", e)

# Example usage
if __name__ == "__main__":
    emp_id = input("Enter Employee ID: ")
    get_employee_details(emp_id)
