using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

namespace RageQuit
{
    class RageQuit
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine();
            string regex = @"(([^\d]+)(\d+))";
            MatchCollection matches = Regex.Matches(input, regex);
            StringBuilder text = new StringBuilder();

            foreach (Match match in matches)
            {
                string message = match.Groups[2].Value;
                int repeats = int.Parse(match.Groups[3].Value);

                for (int i = 0; i < repeats; i++)
                {
                    text.Append(message.ToUpper());
                }
            }

            int count = text.ToString().Distinct().Count();

            Console.WriteLine($"Unique symbols used: {count}");
            Console.WriteLine(text);
        }
    }
}
