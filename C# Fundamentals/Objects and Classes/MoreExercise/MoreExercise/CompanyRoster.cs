using System;
using System.Collections.Generic;
using System.Linq;

namespace CompanyRoster
{
    class CompanyRoster
    {
        static void Main(string[] args)
        {
            int numberOfLines = int.Parse(Console.ReadLine());
            var listOfInfo = new List<Employee>();
            double maxSum = double.MinValue;

            for(int i = 0; i < numberOfLines; i++)
            {
                string[] currentInfo = Console.ReadLine().Split(" ");
                string name = currentInfo[0];
                double salary = double.Parse(currentInfo[1]);
                string department = currentInfo[2];
                double sum = 0;

                Employee employee = new Employee()
                {
                    Name = name,
                    Salary = salary,
                    Department = department
                };     
                
                if(employee.Sum == 0)
                {
                    employee.Sum = salary;
                    employee.MaxSum = salary;
                }

                foreach(Employee current in listOfInfo)
                {
                    if(current.Department == department)
                    {
                        sum = current.Sum + employee.Salary;
                        employee.Sum = sum;

                        if(sum > maxSum)
                        {
                            maxSum = sum;
                            employee.MaxSum = maxSum;
                        }
                    }
                }
                listOfInfo.Add(employee);
            }
            string heightDepartment = String.Empty;
            foreach (Employee employee in listOfInfo)
            {
                if(employee.MaxSum == maxSum)
                {
                    heightDepartment = employee.Department;
                }
            }
            Console.WriteLine($"Highest Average Salary: {heightDepartment}");
            var sortedBySalary = listOfInfo.OrderBy(o => o.Salary).ToList();
            sortedBySalary.Reverse();

            foreach(Employee employee in sortedBySalary)
            {
                if(employee.Department == heightDepartment)
                {
                    Console.WriteLine($"{employee.Name} {employee.Salary:F2}");
                }
            }
        }
    }
}
