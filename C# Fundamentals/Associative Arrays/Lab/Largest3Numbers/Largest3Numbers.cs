using System;
using System.Linq;
using System.Collections.Generic;
using System.Text;

namespace Largest3Numbers
{
    class Largest3Numbers
    {
        static void Main(string[] args)
        {
            //var numberList = Console.ReadLine()
            //    .Split(" ")
            //    .Select(int.Parse)
            //    .ToList()
            //    .OrderByDescending(n => n)
            //    .Take(3)
            //    .ToList();

            //numberList.ForEach(item => Console.Write(item + " "));
            //0.056s

            int[] numbers = Console.ReadLine().Split(" ").Select(int.Parse).OrderByDescending(n => n).ToArray();

            int count = numbers.Length >= 3 ? 3 : numbers.Length;

            for (int i = 0; i < count; i++)
            {
                Console.Write($"{numbers[i]} ");
            }
            // 0.056s

            //if(numbers.Length < 3)
            //{
            //    Console.WriteLine(string.Join(" ", numbers));
            //}
            //else
            //{
            //    StringBuilder result = new StringBuilder();

            //    for (int i = 0; i < 3; i++)
            //    {                    
            //        result.Append(numbers[i]);
            //        result.Append(" ");
            //    }

            //    Console.WriteLine(result);
            //}
            // 0.093s
        }
    }
}
