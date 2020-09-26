using System;
using System.Collections.Generic;
using System.Linq;

namespace CountRealNumbers
{
    class CountRealNumbers
    {
        static void Main(string[] args)
        {
            double[] realNumbers = Console.ReadLine().Split(" ").Select(double.Parse).ToArray();
            var realNumberCount = new SortedDictionary<double, int>();

            foreach(var realNumber in realNumbers)
            {
                if (realNumberCount.ContainsKey(realNumber))
                {
                    realNumberCount[realNumber] = realNumberCount[realNumber] + 1;
                }
                else
                {
                    realNumberCount.Add(realNumber, 1);
                }
            }

            foreach(var realNumber in realNumberCount)
            {
                Console.WriteLine($"{realNumber.Key} -> {realNumber.Value}");
            }
        }
    }
}
