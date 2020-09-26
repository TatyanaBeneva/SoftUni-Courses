using System;
using System.Collections.Generic;
using System.Linq;

namespace Judge
{
    class Judge
    {
        static void Main(string[] args)
        {
            var contestNamePoints = new Dictionary<string, Dictionary<string, int>>();

            while (true)
            {
                string command = Console.ReadLine();

                if (command == "no more time")
                {
                    PrintResultsOfContest(contestNamePoints);
                    PrintIndividualResults(contestNamePoints);
                    break;
                }
                else
                {
                    string[] current = command.Split(" -> ");
                    string personName = current[0];
                    string contestName = current[1];
                    int points = int. Parse(current[2]);
                    AddParticipants(contestNamePoints, personName, contestName, points);
                }
            }
        }

        static void PrintIndividualResults(Dictionary<string, Dictionary<string, int>> contestNamePoints)
        {
            var allPoints = new Dictionary<string, int>();

            foreach (var contest in contestNamePoints)
            {
                foreach (var name in contest.Value)
                {
                    if (allPoints.ContainsKey(name.Key))
                    {
                        foreach (var list in allPoints)
                        {
                            if (name.Key == list.Key)
                            {
                                allPoints[list.Key] += name.Value;
                                break;
                            }
                        }
                    }
                    else
                    {
                        allPoints.Add(name.Key, name.Value);
                    }
                }
            }
                       
            allPoints = allPoints.OrderByDescending(o => o.Value).ThenBy(p => p.Key).ToDictionary(k => k.Key, k => k.Value);
            Console.WriteLine("Individual standings:");
            int count = 0;

            foreach(var list in allPoints)
            {
                count++;
                Console.WriteLine($"{count}. {list.Key} -> {list.Value}");
            }
        }

        static bool IsNameExist(Dictionary<string, int> allPoints, Dictionary<string, Dictionary<string, int>> contestNamePoint)
        {
            foreach(var contest in contestNamePoint)
            {
                foreach( var name in contest.Value)
                {
                    foreach(var list in allPoints)
                    {
                        if(list.Key == name.Key)
                        {
                            return true;
                        }
                    }
                }
            }

            return false;
        }

        static void PrintResultsOfContest(Dictionary<string, Dictionary<string, int>> contestNamePoints)
        {
            var list = new Dictionary<string, int>();

            foreach(var contest in contestNamePoints)
            {
                int count = 0;

                foreach(var name in contest.Value)
                {
                    list.Add(name.Key, name.Value);
                    count++;
                }

                Console.WriteLine($"{contest.Key}: {count} participants");
                list = list.OrderByDescending(o => o.Value).ThenBy(n => n.Key).ToDictionary(k => k.Key, k => k.Value);
                count = 0;

                foreach(var name in list)
                {
                    count++;
                    Console.WriteLine($"{count}. {name.Key} <::> {name.Value}");
                }

                foreach(var name in contest.Value)
                {
                    list.Remove(name.Key);
                }
            }
        }

        static void AddParticipants(Dictionary<string, Dictionary<string, int>> contestNamePoints,
            string personName,
            string contestName,
            int points)
        {
            if(IsContestExist(contestNamePoints, contestName) == false)
            {
                var list = new Dictionary<string, int>();
                list.Add(personName, points);
                contestNamePoints.Add(contestName, list);
            }
            else
            {
                if(IsTheParticipantExistInCurrentContest(contestNamePoints, personName, contestName) == false)
                {
                    Dictionary<string, int> list = contestNamePoints[contestName];
                    list.Add(personName, points);
                }
                else
                {
                    if(IsPointsMore(contestNamePoints, personName, contestName, points) == true)
                    {
                        Dictionary<string, int> list = contestNamePoints[contestName];
                        list[personName] = points;
                    }
                }
            }
        }

        static bool IsPointsMore(Dictionary<string, Dictionary<string, int>> contestNamePoints,
            string personName,
            string contestName,
            int points)
        {
            foreach (var contest in contestNamePoints)
            {
                if (contest.Key == contestName)
                {
                    foreach (var name in contest.Value)
                    {
                        if(name.Key == personName)
                        {
                            if(name.Value < points)
                            {
                                return true;
                            }
                        }
                    }
                }
            }

            return false;
        }

        static bool IsTheParticipantExistInCurrentContest(Dictionary<string, Dictionary<string, int>> contestNamePoints,
            string personName,
            string contestName)
        {
            foreach(var contest in contestNamePoints)
            {
                if(contest.Key == contestName)
                {
                    foreach(var name in contest.Value)
                    {
                        if(name.Key == personName)
                        {
                            return true;
                        }
                    }
                }
            }

            return false;
        }

        static bool IsContestExist(Dictionary<string, Dictionary<string, int>> contestNamePoints,
            string contestName)
        {
            if (contestNamePoints.ContainsKey(contestName))
            {
                return true;
            }

            return false;

        }
    }
}
