using System;
using System.Linq;

namespace SumEvenNumbers
{
    class SumEvenNumbers
    {
        static void Main(string[] args)
        {
            int[] input = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int sum = 0;

            for (int i = 0; i < input.Length; i++)
            {
                int curentNumber = input[i];
                if(curentNumber % 2 == 0)
                {
                    sum += curentNumber;
                }
            }

            Console.WriteLine(sum);
        }
    }
}
