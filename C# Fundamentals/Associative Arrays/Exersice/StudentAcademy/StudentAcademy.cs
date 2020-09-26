using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace StudentAcademy
{
    class StudentAcademy
    {
        static void Main(string[] args)
        {
            int numberOfLines = int.Parse(Console.ReadLine());
            var listOfStudents = new Dictionary<string, List<double>>();

            for(int i = 0; i< numberOfLines; i++)
            {
                string name = Console.ReadLine();
                double grade = double.Parse(Console.ReadLine());

                AddStudents(listOfStudents, name, grade);
            }
            AverageGrade(listOfStudents);

            listOfStudents = listOfStudents.OrderByDescending(o => o.Value[0]).Where(o => o.Value[0] >= 4.50).ToDictionary(o => o.Key, o => o.Value);

            foreach(var student in listOfStudents)
            {
                Console.WriteLine($"{student.Key} -> {student.Value[0]:f2}");
            }
        }

        static void AverageGrade(Dictionary<string, List<double>> listOfStudents)
        {
            foreach (var student in listOfStudents)
            {
                double averageGrade = student.Value.Average();

                if (student.Value.Count > 1)
                {
                    for (int i = 0; i < student.Value.Count; i++)
                    {
                        student.Value.RemoveAt(0);
                    }
                }

                student.Value.Add(averageGrade);
                student.Value.RemoveAt(0);
            }
        }

        static void AddStudents(Dictionary<string, List<double>> listOfStudents,
            string name,
            double grade)
        {
            if(IsStudentExist(listOfStudents, name) == true)
            {
                List<double> list = listOfStudents[name];
                list.Add(grade);
            }
            else
            {
                listOfStudents.Add(name, new List<double> { grade });
            }
        }

        static bool IsStudentExist(Dictionary<string, List<double>> listOfStudents,
            string name)
        {
            if (listOfStudents.ContainsKey(name))
            {
                return true;
            }

            return false;
        }
    }
}
