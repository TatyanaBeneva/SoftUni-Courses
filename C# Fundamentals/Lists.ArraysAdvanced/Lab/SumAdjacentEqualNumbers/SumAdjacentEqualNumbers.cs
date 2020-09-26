using System;
using System.Collections.Generic;
using System.Linq;

namespace SumAdjacentEqualNumbers
{
    class SumAdjacentEqualNumbers
    {
        static void Main(string[] args)
        {
            List<double> numbers = Console.ReadLine().Split(" ").Select(double.Parse).ToList();
            SumOfEqualNumbers(numbers);
        }

        static void SumOfEqualNumbers(List<double> numbers)
        {
            for(int i = 0; i < numbers.Count; i++)
            {
                if(numbers.Count <= i + 1)
                {
                    break;
                }

                double numberOfIndex = numbers[i];
                double numberAfterIndex = numbers[i + 1];

                if(numberOfIndex == numberAfterIndex)
                {
                    numbers[i] = numberOfIndex + numberAfterIndex;
                    numbers.RemoveAt(i + 1);
                    i = -1;
                }
            }

            Console.WriteLine(string.Join(" ", numbers));
        }
    }
}
