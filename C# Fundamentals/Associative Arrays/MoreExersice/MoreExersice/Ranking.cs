using System;
using System.Linq;
using System.Collections.Generic;

namespace Ranking
{
    class Ranking
    {
        static void Main(string[] args)
        {
            var nameOfContestAndPassword = new Dictionary<string, string>();
            var nameAndPoints = new Dictionary<string, Dictionary<string, int>>();
            

            while (true)
            {
                string command = Console.ReadLine();

                if (command == "end of contests")
                {
                    break;
                }
                else
                {
                    string[] current = command.Split(":");
                    string nameOfContest = current[0];
                    string passwordOfContest = current[1];
                    nameOfContestAndPassword.Add(nameOfContest, passwordOfContest);
                }
            }
           
            while (true)
            {
                string command = Console.ReadLine();
                if (command == "end of submissions")
                {
                    break;
                }
                else
                {
                    string[] current = command.Split("=>");
                    string nameOfContest = current[0];
                    string passwordOfContest = current[1];
                    string userName = current[2];
                    int points = int.Parse(current[3]);
                    AddNameAndPoints(nameOfContestAndPassword, nameAndPoints, nameOfContest, passwordOfContest, userName, points);
                }
            }

            BestSumOfPoints(nameAndPoints);
            PrintTheResult(nameAndPoints);
        }

        static void PrintTheResult(Dictionary<string, Dictionary<string, int>> nameAndPoints)
        {
            Console.WriteLine("Ranking: ");

            nameAndPoints = nameAndPoints.OrderBy(o => o.Key).ToDictionary(k => k.Key, k => k.Value);
            var past = new Dictionary<string, int>();

            foreach (var name in nameAndPoints)
            {
                Console.WriteLine(name.Key);
                
                foreach(var dict in name.Value)
                {
                    past.Add(dict.Key, dict.Value);
                }

                past = past.OrderByDescending(o => o.Value).ToDictionary(k => k.Key, k => k.Value);
                foreach(var dict in past)
                {
                    Console.WriteLine($"#  {dict.Key} -> {dict.Value}");
                }

                foreach(var dict in name.Value)
                {
                    past.Remove(dict.Key);
                }
            }           
        }

        static void BestSumOfPoints(Dictionary<string, Dictionary<string, int>> nameAndPoints)
        {
            int max = 0;
            string name = string.Empty;
            
            foreach(var names in nameAndPoints)
            {
                int sum = 0;

                foreach(var list in names.Value)
                {
                    sum += list.Value;
                }

                if(sum > max)
                {
                    max = sum;
                    name = names.Key;
                }
            }

            Console.WriteLine($"Best candidate is {name} with total {max} points.");
        }

        static void AddNameAndPoints(Dictionary<string, string> nameOfContestAndPassword,
            Dictionary<string, Dictionary<string, int>> nameAndPoints,
            string nameOfContest,
            string passwordOfContest,
            string userName,
            int points)
        {
            if(IsContestValid(nameOfContestAndPassword, nameOfContest) == true && 
                IsPasswordValid(nameOfContestAndPassword, nameOfContest, passwordOfContest) == true)
            {
                if(IsNameExist(nameAndPoints, userName) == false)
                {
                    var list = new Dictionary<string, int>();
                    list.Add(nameOfContest, points);
                    nameAndPoints.Add(userName, list);
                }
                else
                {
                    if(IsTheUserHavePointToCurrentContest(nameAndPoints, nameOfContest, userName) == false)
                    {
                        Dictionary<string, int> list = nameAndPoints[userName];
                        list.Add(nameOfContest, points);
                    }
                    else
                    {
                        if(IsTheNewPointAreMore(nameAndPoints, nameOfContest, userName, points) == true)
                        {
                            Dictionary<string, int> list = nameAndPoints[userName];
                            list[nameOfContest] = points;
                        }
                    }
                }
            }
        }

        static bool IsNameExist(Dictionary<string, Dictionary<string, int>> nameAndPoints, string userName)
        {
            if (nameAndPoints.ContainsKey(userName))
            {
                return true;
            }

            return false;
        }

        static bool IsContestValid(Dictionary<string, string> nameOfContestAndPassword, string nameOfContest)
        {
            if (nameOfContestAndPassword.ContainsKey(nameOfContest))
            {
                return true;
            }

            return false;
        }

        static bool IsPasswordValid(Dictionary<string, string> nameOfContestAndPassword,
            string nameOfContest,
            string password)
        {
            foreach(var contest in nameOfContestAndPassword)
            {
                if(contest.Key == nameOfContest)
                {
                    if(contest.Value == password)
                    {
                        return true;
                    }
                }
            }

            return false;
        }

        static bool IsTheUserHavePointToCurrentContest(Dictionary<string, Dictionary<string, int>> nameAndPoints,
            string nameOfContest,
            string userName)
        {
            foreach(var name in nameAndPoints)
            {
                if(name.Key == userName)
                {
                    foreach(var list in name.Value)
                    {
                        if (list.Key == nameOfContest)
                        {
                            return true;
                        }
                    }
                }
            }

            return false;
        }

        static bool IsTheNewPointAreMore(Dictionary<string, Dictionary<string, int>> nameAndPoints,
            string nameOfContest,
            string userName,
            int points)
        {
            if (IsTheUserHavePointToCurrentContest(nameAndPoints, nameOfContest, userName) == true)
            {
                foreach (var name in nameAndPoints)
                {
                    if (name.Key == userName)
                    {
                        foreach (var list in name.Value)
                        {
                            if (list.Key == nameOfContest)
                            {
                                if (list.Value < points)
                                {
                                    return true;
                                }
                            }
                        }
                    }
                }
            }

            return false;
        }
        
    }
}
