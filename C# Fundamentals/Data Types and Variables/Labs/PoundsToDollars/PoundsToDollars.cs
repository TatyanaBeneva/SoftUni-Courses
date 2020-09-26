using System;

namespace PoundsToDollars
{
    class PoundsToDollars
    {
        static void Main(string[] args)
        {
            var pounds = decimal.Parse(Console.ReadLine());
            decimal dollars = pounds * 1.31m;
            Console.WriteLine($"{dollars:F3}");
        }
    }
}
