using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Race
{
    class Race
    {
        static void Main(string[] args)
        {
            string participants = Console.ReadLine();
            Dictionary<string, int> contestResults = new Dictionary<string, int>();
            string regexName = @"[A-Za-z]";
            string regexDigits = @"\d";

            while (true)
            {
                string command = Console.ReadLine();

                if(command == "end of race")
                {
                    break;
                }
                else
                {
                    MatchCollection name = Regex.Matches(command, regexName);
                    string currentName = string.Join("", name);

                    if (participants.Contains(currentName))
                    {
                        MatchCollection digits = Regex.Matches(command, regexDigits);
                        int sum = 0;

                        foreach(Match match in digits)
                        {
                            sum += int.Parse(match.ToString());
                        }

                        if(IsNameExist(contestResults, currentName) == true)
                        {
                            contestResults[currentName] += sum;
                        }
                        else
                        {
                            contestResults.Add(currentName, sum);
                        }
                    }
                }
            }

            contestResults = contestResults.OrderByDescending(o => o.Value).Take(3).ToDictionary(k => k.Key, k => k.Value);

            List<string> names = new List<string>();

            foreach(var result in contestResults)
            {
                names.Add(result.Key);
            }

            Console.WriteLine($"1st place: {names[0].ToString()}");
            Console.WriteLine($"2nd place: {names[1].ToString()}");
            Console.WriteLine($"3rd place: {names[2].ToString()}");

        }

        static bool IsNameExist(Dictionary<string, int> contestResults, string currentName)
        {
            if (contestResults.ContainsKey(currentName))
            {
                return true;
            }

            return false;
        }
    }
}
