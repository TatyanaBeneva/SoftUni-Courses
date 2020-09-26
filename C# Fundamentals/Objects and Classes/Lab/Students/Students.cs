using System;
using System.Collections.Generic;

namespace Students
{
    class Students
    {
        static void Main(string[] args)
        {
            var studentsList = new List<Student>();
            string command = Console.ReadLine();

            while (command != "end")
            {
                string[] currentStudantInformation = command.Split(" ");

                string firtsName = currentStudantInformation[0];
                string lastName = currentStudantInformation[1];
                int age = int.Parse(currentStudantInformation[2]);
                string homeTown = currentStudantInformation[3];

                if(IsStudentExist(studentsList, firtsName, lastName) == true)
                {
                    Student currentStudent = GetStudent(studentsList, firtsName, lastName);

                    currentStudent.FirstName = firtsName;
                    currentStudent.LastName = lastName;
                    currentStudent.Age = age;
                    currentStudent.HomeTown = homeTown;
                }
                else
                {
                    Student currentStudent = new Student()
                    {
                        FirstName = firtsName,
                        LastName = lastName,
                        Age = age,
                        HomeTown = homeTown
                    };

                    studentsList.Add(currentStudent);
                }

                command = Console.ReadLine();
            }

            string choicenTown = Console.ReadLine();

            foreach(Student student in studentsList)
            {
                if(student.HomeTown == choicenTown)
                {
                    Console.WriteLine($"{student.FirstName} {student.LastName} is {student.Age} years old.");
                }
            }
        }

        static bool IsStudentExist(List<Student> studentsList, string firstName, string lastName)
        {
            foreach(Student student in studentsList)
            {
                if(student.FirstName == firstName && student.LastName == lastName)
                {
                    return true;
                }
            }

            return false;
        }

        static Student GetStudent(List<Student> studentsList, string firstName, string lastName)
        {
            Student existingStudent = null;

            foreach(Student student in studentsList)
            {
                if (student.FirstName == firstName && student.LastName == lastName)
                {
                    existingStudent = student;
                }
            }

            return existingStudent;
        }
    }
}
