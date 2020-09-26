using System;
using System.Text.RegularExpressions;

namespace ExtractEmails
{
    class ExtractEmails
    {
        static void Main(string[] args)
        {
            string regex = @"\s(([0-9A-Za-z][\.-0-9a-zA-Z]*[A-Za-z0-9])|([a-zA-z0-9]))@(([A-Za-z][-a-zA-Z]*[A-Za-z])|([A-Za-z]))(\.(([A-Za-z][-a-zA-Z]*[A-Za-z])|([A-Za-z])))+";
            string text = Console.ReadLine();
            MatchCollection matches = Regex.Matches(text, regex);
            
            if(matches.Count > 0)
            {
                foreach(Match result in matches)
                {
                    Console.WriteLine(result);
                }
            }
        }
    }
}
