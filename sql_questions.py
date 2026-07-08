sql_questions = [

    {
        "title":"Select All Records",
        "topic":"SELECT",
        "difficulty":"Easy",
        "description":"Write a query to display all records from the Employee table.",
        "input":"Employee(EmpID, Name, Salary)",
        "output":"All employee records",
        "solution":"SELECT * FROM Employee;"
    },

    {
        "title":"Select Specific Columns",
        "topic":"SELECT",
        "difficulty":"Easy",
        "description":"Display only Name and Salary from Employee table.",
        "input":"Employee(EmpID, Name, Salary)",
        "output":"Name, Salary",
        "solution":"SELECT Name, Salary FROM Employee;"
    },

    {
        "title":"Employees with Salary Greater than 50000",
        "topic":"WHERE",
        "difficulty":"Easy",
        "description":"Display employees whose salary is greater than 50000.",
        "input":"Employee(EmpID, Name, Salary)",
        "output":"Matching employees",
        "solution":"SELECT * FROM Employee WHERE Salary > 50000;"
    },

    {
        "title":"Sort Employees by Salary",
        "topic":"ORDER BY",
        "difficulty":"Easy",
        "description":"Display all employees sorted by salary in descending order.",
        "input":"Employee(EmpID, Name, Salary)",
        "output":"Employees sorted by Salary",
        "solution":"SELECT * FROM Employee ORDER BY Salary DESC;"
    },

    {
        "title":"Distinct Departments",
        "topic":"DISTINCT",
        "difficulty":"Easy",
        "description":"Display all unique department names.",
        "input":"Employee(EmpID, Name, Department)",
        "output":"Unique Departments",
        "solution":"SELECT DISTINCT Department FROM Employee;"
    },

    {
        "title":"Names Starting with A",
        "topic":"LIKE",
        "difficulty":"Easy",
        "description":"Display employees whose name starts with A.",
        "input":"Employee(EmpID, Name)",
        "output":"Employees starting with A",
        "solution":"SELECT * FROM Employee WHERE Name LIKE 'A%';"
    },

    {
        "title":"Salary Between 30000 and 60000",
        "topic":"BETWEEN",
        "difficulty":"Easy",
        "description":"Display employees having salary between 30000 and 60000.",
        "input":"Employee(EmpID, Name, Salary)",
        "output":"Matching employees",
        "solution":"SELECT * FROM Employee WHERE Salary BETWEEN 30000 AND 60000;"
    },

    {
        "title":"Employees from IT or HR",
        "topic":"IN",
        "difficulty":"Easy",
        "description":"Display employees working in IT or HR department.",
        "input":"Employee(EmpID, Name, Department)",
        "output":"Employees from IT and HR",
        "solution":"SELECT * FROM Employee WHERE Department IN ('IT','HR');"
    },

    {
        "title":"Count Total Employees",
        "topic":"COUNT",
        "difficulty":"Easy",
        "description":"Find the total number of employees.",
        "input":"Employee(EmpID)",
        "output":"Employee Count",
        "solution":"SELECT COUNT(*) FROM Employee;"
    },

    {
        "title":"Average Salary",
        "topic":"AVG",
        "difficulty":"Easy",
        "description":"Find the average salary of employees.",
        "input":"Employee(EmpID, Salary)",
        "output":"Average Salary",
        "solution":"SELECT AVG(Salary) FROM Employee;"
    },
        {
        "title":"Total Salary Department Wise",
        "topic":"GROUP BY",
        "difficulty":"Medium",
        "description":"Find the total salary of employees in each department.",
        "input":"Employee(EmpID, Name, Department, Salary)",
        "output":"Department | Total Salary",
        "solution":"SELECT Department, SUM(Salary) AS TotalSalary FROM Employee GROUP BY Department;"
    },

    {
        "title":"Departments Having More Than 5 Employees",
        "topic":"HAVING",
        "difficulty":"Medium",
        "description":"Display departments having more than 5 employees.",
        "input":"Employee(EmpID, Name, Department)",
        "output":"Department Names",
        "solution":"SELECT Department, COUNT(*) FROM Employee GROUP BY Department HAVING COUNT(*) > 5;"
    },

    {
        "title":"Total Salary",
        "topic":"SUM",
        "difficulty":"Easy",
        "description":"Find the total salary of all employees.",
        "input":"Employee(EmpID, Salary)",
        "output":"Total Salary",
        "solution":"SELECT SUM(Salary) FROM Employee;"
    },

    {
        "title":"Minimum Salary",
        "topic":"MIN",
        "difficulty":"Easy",
        "description":"Find the minimum salary in the Employee table.",
        "input":"Employee(EmpID, Salary)",
        "output":"Minimum Salary",
        "solution":"SELECT MIN(Salary) FROM Employee;"
    },

    {
        "title":"Maximum Salary",
        "topic":"MAX",
        "difficulty":"Easy",
        "description":"Find the maximum salary in the Employee table.",
        "input":"Employee(EmpID, Salary)",
        "output":"Maximum Salary",
        "solution":"SELECT MAX(Salary) FROM Employee;"
    },

    {
        "title":"Inner Join",
        "topic":"INNER JOIN",
        "difficulty":"Medium",
        "description":"Display employee name and department name using INNER JOIN.",
        "input":"Employee(EmpID, Name, DeptID), Department(DeptID, DeptName)",
        "output":"Employee Name | Department Name",
        "solution":"SELECT Employee.Name, Department.DeptName FROM Employee INNER JOIN Department ON Employee.DeptID = Department.DeptID;"
    },

    {
        "title":"Left Join",
        "topic":"LEFT JOIN",
        "difficulty":"Medium",
        "description":"Display all employees with their department names.",
        "input":"Employee(EmpID, Name, DeptID), Department(DeptID, DeptName)",
        "output":"All Employees",
        "solution":"SELECT Employee.Name, Department.DeptName FROM Employee LEFT JOIN Department ON Employee.DeptID = Department.DeptID;"
    },

    {
        "title":"Right Join",
        "topic":"RIGHT JOIN",
        "difficulty":"Medium",
        "description":"Display all departments even if they have no employees.",
        "input":"Employee(EmpID, Name, DeptID), Department(DeptID, DeptName)",
        "output":"All Departments",
        "solution":"SELECT Employee.Name, Department.DeptName FROM Employee RIGHT JOIN Department ON Employee.DeptID = Department.DeptID;"
    },

    {
        "title":"Full Join",
        "topic":"FULL JOIN",
        "difficulty":"Hard",
        "description":"Display all employees and departments.",
        "input":"Employee(EmpID, Name, DeptID), Department(DeptID, DeptName)",
        "output":"Complete Records",
        "solution":"SELECT Employee.Name, Department.DeptName FROM Employee FULL OUTER JOIN Department ON Employee.DeptID = Department.DeptID;"
    },

    {
        "title":"Self Join",
        "topic":"SELF JOIN",
        "difficulty":"Hard",
        "description":"Display employee name with their manager name.",
        "input":"Employee(EmpID, Name, ManagerID)",
        "output":"Employee | Manager",
        "solution":"SELECT E.Name AS Employee, M.Name AS Manager FROM Employee E LEFT JOIN Employee M ON E.ManagerID = M.EmpID;"
    },
        {
        "title":"UNION",
        "topic":"UNION",
        "difficulty":"Medium",
        "description":"Combine employee names from Employee and Manager tables without duplicates.",
        "input":"Employee(Name), Manager(Name)",
        "output":"Unique Names",
        "solution":"SELECT Name FROM Employee UNION SELECT Name FROM Manager;"
    },

    {
        "title":"UNION ALL",
        "topic":"UNION ALL",
        "difficulty":"Medium",
        "description":"Combine employee names from Employee and Manager tables including duplicates.",
        "input":"Employee(Name), Manager(Name)",
        "output":"All Names",
        "solution":"SELECT Name FROM Employee UNION ALL SELECT Name FROM Manager;"
    },

    {
        "title":"Subquery",
        "topic":"Subquery",
        "difficulty":"Medium",
        "description":"Display employees whose salary is greater than the average salary.",
        "input":"Employee(EmpID, Name, Salary)",
        "output":"Employees with salary above average",
        "solution":"SELECT * FROM Employee WHERE Salary > (SELECT AVG(Salary) FROM Employee);"
    },

    {
        "title":"EXISTS",
        "topic":"EXISTS",
        "difficulty":"Hard",
        "description":"Display customers who have placed at least one order.",
        "input":"Customer(CustomerID, Name), Orders(OrderID, CustomerID)",
        "output":"Customer Names",
        "solution":"SELECT * FROM Customer C WHERE EXISTS (SELECT 1 FROM Orders O WHERE O.CustomerID = C.CustomerID);"
    },

    {
        "title":"CASE Statement",
        "topic":"CASE",
        "difficulty":"Medium",
        "description":"Display employee salary grade using CASE.",
        "input":"Employee(Name, Salary)",
        "output":"Name | Grade",
        "solution":"SELECT Name, CASE WHEN Salary>=70000 THEN 'A' WHEN Salary>=50000 THEN 'B' ELSE 'C' END AS Grade FROM Employee;"
    },

    {
        "title":"Create View",
        "topic":"VIEW",
        "difficulty":"Medium",
        "description":"Create a view containing employee names and salaries.",
        "input":"Employee(Name, Salary)",
        "output":"EmployeeView",
        "solution":"CREATE VIEW EmployeeView AS SELECT Name, Salary FROM Employee;"
    },

    {
        "title":"Create Index",
        "topic":"INDEX",
        "difficulty":"Medium",
        "description":"Create an index on the Name column of Employee table.",
        "input":"Employee(Name)",
        "output":"Index Created",
        "solution":"CREATE INDEX idx_employee_name ON Employee(Name);"
    },

    {
        "title":"ROW_NUMBER()",
        "topic":"Window Function",
        "difficulty":"Hard",
        "description":"Assign row numbers to employees based on salary.",
        "input":"Employee(Name, Salary)",
        "output":"Row Number",
        "solution":"SELECT Name, Salary, ROW_NUMBER() OVER(ORDER BY Salary DESC) AS RowNum FROM Employee;"
    },

    {
        "title":"RANK()",
        "topic":"Window Function",
        "difficulty":"Hard",
        "description":"Rank employees according to salary.",
        "input":"Employee(Name, Salary)",
        "output":"Salary Rank",
        "solution":"SELECT Name, Salary, RANK() OVER(ORDER BY Salary DESC) AS RankNo FROM Employee;"
    },

    {
        "title":"Common Table Expression (CTE)",
        "topic":"CTE",
        "difficulty":"Hard",
        "description":"Use a CTE to display employees earning more than 50000.",
        "input":"Employee(Name, Salary)",
        "output":"Matching Employees",
        "solution":"WITH HighSalary AS (SELECT * FROM Employee WHERE Salary > 50000) SELECT * FROM HighSalary;"
    }

]