﻿using System;
using System.Text.RegularExpressions;

namespace MatchDates
{
    class MatchDates
    {
        static void Main(string[] args)
        {
            var regex = @"\b(?<day>\d{2})([-.\/])(?<month>[A-Z][a-z]{2})\1(?<year>\d{4})\b";
            var dates = Console.ReadLine();
            MatchCollection goodDates = Regex.Matches(dates, regex);

            foreach(Match date in goodDates)
            {
                var day = date.Groups["day"].Value;
                var month = date.Groups["month"].Value;
                var year = date.Groups["year"].Value;
                Console.WriteLine($"Day: {day}, Month: {month}, Year: {year}");
            }
        }
    }
}
