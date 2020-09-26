using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace SoftUniBarIncome
{
    class SoftUniBarIncome
    {
        static void Main(string[] args)
        {
            double totalSum = 0.0;
            string regex = @"^%(?<name>[A-Z][a-z]+)%[^|$%.]*<(?<product>\w+)>[^|$%.]*\|(?<count>\d+)\|[^|$%.]*?(?<price>\d*\.?\d*)\$";

            while (true)
            {
                string command = Console.ReadLine();
                if(command == "end of shift")
                {
                    Console.WriteLine($"Total income: {totalSum:f2}");
                    break;
                }
                else
                {
                    Match name = Regex.Match(command, regex);

                    if (name.Success)
                    {
                        string currentName = name.Groups["name"].Value;
                        string currentProduct = name.Groups["product"].Value;
                        int currentCount = int.Parse(name.Groups["count"].Value);
                        double currentPrice = double.Parse(name.Groups["price"].Value);
                        double sum = currentPrice * currentCount;
                        Console.WriteLine($"{currentName}: {currentProduct} - {sum:F2}");
                        totalSum += sum;
                    }
                }
            }
        }
    }
}
