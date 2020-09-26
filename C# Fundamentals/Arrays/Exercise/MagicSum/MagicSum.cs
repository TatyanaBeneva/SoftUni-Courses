using System;
using System.Linq;
namespace MagicSum
{
    class MagicSum
    {
        static void Main(string[] args)
        {
            int[] numbers = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
            int sumNumber = int.Parse(Console.ReadLine());

            for(int i = 0; i < numbers.Length - 1; i++)
            {
                int sum = 0;

                for (int j = (i + 1); j < numbers.Length; j++)
                {
                    sum = numbers[i] + numbers[j];

                    if(sum == sumNumber)
                    {
                        Console.WriteLine(numbers[i] + " " + numbers[j]);
                    }
                }
            }
        }
    }
}
