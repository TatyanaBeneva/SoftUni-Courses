using System;
using System.Text.RegularExpressions;

namespace MatchFullName
{
    class MatchFullName
    {
        static void Main(string[] args)
        {
            string regex = @"\b[A-Z][a-z]+ [A-Z][a-z]+\b";
            string names = Console.ReadLine();

            MatchCollection matchedName = Regex.Matches(names, regex);
            Console.WriteLine(string.Join(" ", matchedName));
        }
    }
}
