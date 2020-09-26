using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Courses
{
    class Courses
    {
        static void Main(string[] args)
        {
            var courseInfo = new Dictionary<string, List<string>>();

            while (true)
            {
                string command = Console.ReadLine();

                if(command == "end")
                {
                    break;
                }
                else
                {
                    string[] currentCours = command.Split(" : ");
                    AddCourses(courseInfo, currentCours);
                }
            }

            courseInfo = courseInfo.OrderByDescending(o => o.Value.Count).ToDictionary(o => o.Key, o => o.Value);

            foreach(var course in courseInfo)
            {
                Console.WriteLine($"{course.Key}: {course.Value.Count}");

                course.Value.OrderBy(o => o).ToList().ForEach(o => Console.WriteLine($"-- {o}"));
            }
        }

        static void AddCourses(Dictionary<string, List<string>> courseInfo, string[] currentCours)
        {
            if(IsCoursExist(courseInfo, currentCours) == true)
            {
                List<string> list = courseInfo[currentCours[0]];
                list.Add(currentCours[1]);
            }
            else
            {
                courseInfo.Add(currentCours[0], new List<string> { currentCours[1] });
            }
        }

        static bool IsCoursExist(Dictionary<string, List<string>> courseInfo, string[] currentCours)
        {
            if (courseInfo.ContainsKey(currentCours[0]))
            {
                return true;
            }

            return false;
        }
    }
}
