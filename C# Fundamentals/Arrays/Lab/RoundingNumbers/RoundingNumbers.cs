using System;
using System.Linq;

namespace RoundingNumbers
{
    class RoundingNumbers
    {
        static void Main(string[] args)
        {
            double[] input = Console.ReadLine()
                .Split()
                .Select(double.Parse)
                .ToArray();

            for(int i = 0; i < input.Length; i++)
            {
                double splitNumbers = input[i];
                double roundedNumbers = Math.Round(splitNumbers, MidpointRounding.AwayFromZero);
                
                Console.WriteLine($"{Convert.ToDecimal(input[i])} => {Convert.ToDecimal(roundedNumbers)}");
            }
        }
    }
}
