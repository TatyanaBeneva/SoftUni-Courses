using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SoftUniExamResults
{
    class SoftUniExamResults
    {
        static void Main(string[] args)
        {
            var lengAndCount = new Dictionary<string, int>();
            var nameAndPoints = new Dictionary<string, int>();

            while (true)
            {
                string currentCommand = Console.ReadLine();
                
                if(currentCommand == "exam finished")
                {
                    PrintResult(nameAndPoints, lengAndCount);
                    break;
                }
                else if(currentCommand.Contains("banned"))
                {
                    string[] command = currentCommand.Split("-");
                    string name = command[0];
                    nameAndPoints.Remove(name);
                }
                else
                {
                    string[] command = currentCommand.Split("-");
                    string name = command[0];
                    string leng = command[1];
                    int points = int.Parse(command[2]);
                    AddResults(nameAndPoints, lengAndCount, name, leng, points);
                }

            }
        }

        static void PrintResult(Dictionary<string, int> nameAndPoints,
            Dictionary<string, int> lengAndCount)
        {
            nameAndPoints = nameAndPoints.OrderByDescending(o => o.Value).ThenBy(n => n.Key)
                .ToDictionary(m => m.Key, m => m.Value);
            lengAndCount = lengAndCount.OrderByDescending(o => o.Value).ThenBy(n => n.Key)
                .ToDictionary(m => m.Key, m => m.Value);

            Console.WriteLine("Results:");

            foreach(var name in nameAndPoints)
            {
                Console.WriteLine($"{name.Key} | {name.Value}");
            }

            Console.WriteLine("Submissions:");

            foreach(var leng in lengAndCount)
            {
                Console.WriteLine($"{leng.Key} - {leng.Value}");
            }
        }

        static void AddResults(Dictionary<string, int> nameAndPoints,
            Dictionary<string, int> lengAndCount,
            string name, string leng, int points)
        {
            if(IsLengExist(lengAndCount, leng) == true)
            {
                if(IsNameExist(nameAndPoints, name) == true)
                {
                    if(IsPointsMore(nameAndPoints, name, points) == true)
                    {
                        nameAndPoints[name] = points;
                        lengAndCount[leng]++;
                        return;
                    }

                    lengAndCount[leng]++;
                    return;
                }

                lengAndCount[leng]++;
                nameAndPoints.Add(name, points);
            }
            else
            {
                lengAndCount.Add(leng, 1);
                nameAndPoints.Add(name, points);
            }
        }

        static bool IsNameExist(Dictionary<string, int> nameAndPoints, string name)
        {
            if (nameAndPoints.ContainsKey(name))
            {
                return true;
            }

            return false;
        }

        static bool IsLengExist(Dictionary<string, int> lengAndCount, string leng)
        {
            if (lengAndCount.ContainsKey(leng))
            {
                return true;
            }

            return false;
        }

        static bool IsPointsMore(Dictionary<string, int> nameAndPoints, string name, int points)
        {
            foreach(var result in nameAndPoints)
            {
                if(result.Key == name)
                {
                    if(result.Value < points)
                    {
                        return true;
                    }
                }
            }

            return false;
        }
    }
}
