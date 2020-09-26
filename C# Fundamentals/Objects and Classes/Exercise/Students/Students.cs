using System;
using System.Linq;
using System.Collections.Generic;

namespace Students
{
    class Students
    {
        static void Main(string[] args)
        {
            int countOfStudents = int.Parse(Console.ReadLine());
            var listOfStudents = new List<Student>();

            for(int i = 0; i < countOfStudents; i++)
            {
                string[] input = Console.ReadLine().Split(" ");

                string firstName = input[0];
                string lastName = input[1];
                float grade = float.Parse(input[2]);

                Student currentStudent = new Student()
                {
                    FirstName = firstName,
                    LastName = lastName,
                    Grade = grade
                };

                listOfStudents.Add(currentStudent);
            }

            var orderdListOfStudentsByGrade = new List<Student>();
            orderdListOfStudentsByGrade = listOfStudents.OrderBy(o => o.Grade).ToList();
            orderdListOfStudentsByGrade.Reverse();

            foreach(Student student in orderdListOfStudentsByGrade)
            {
                Console.WriteLine($"{student.FirstName} {student.LastName}: {student.Grade:F2}");
            }
        }
    }
}
