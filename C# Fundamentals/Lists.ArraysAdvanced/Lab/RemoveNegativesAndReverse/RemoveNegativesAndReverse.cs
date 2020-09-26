using System;
using System.Collections.Generic;
using System.Linq;


namespace RemoveNegativesAndReverse
{
    class RemoveNegativesAndReverse
    {
        static void Main(string[] args)
        {
            List<int> listOfNumbers = Console.ReadLine().Split(" ").Select(int.Parse).ToList();
            RemoveNegativesNumberAndReverse(listOfNumbers);
        }

        static void RemoveNegativesNumberAndReverse(List<int> listOfNumbers)
        {
            for(int i = 0; i < listOfNumbers.Count; i++)
            {
                if(i < listOfNumbers.Count && listOfNumbers[i] < 0)
                {
                    listOfNumbers.RemoveAt(i--);
                }
            }

            listOfNumbers.Reverse();

            if(listOfNumbers.Count < 1)
            {
                Console.WriteLine("empty");
            }
            else
            {
                Console.WriteLine(string.Join(" ", listOfNumbers));
            }
        }
    }
}
