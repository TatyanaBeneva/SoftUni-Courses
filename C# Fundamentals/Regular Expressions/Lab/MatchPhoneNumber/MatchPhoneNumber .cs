using System;
using System.Text.RegularExpressions;

namespace MatchPhoneNumber
{
    class MatchPhoneNumber
    {
        static void Main(string[] args)
        {
            string regex = @"(?<prefix>\+359)(?<delimeter>[ -])(?<areaCode>2)\k<delimeter>(?<threeNums>\d{3})\k<delimeter>(?<lastFourNums>\d{4})\b";
            string phones = Console.ReadLine();

            MatchCollection matchedPhones = Regex.Matches(phones, regex);
            Console.WriteLine(string.Join(", ", matchedPhones));
        }
    }
}
