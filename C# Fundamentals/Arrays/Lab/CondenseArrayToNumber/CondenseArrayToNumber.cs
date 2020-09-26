using System;
using System.Linq;
namespace CondenseArrayToNumber
{
    class CondenseArrayToNumber
    {
        static void Main(string[] args)
        {
            int[] numbers = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int lastSum = 0;
            int originalLength = numbers.Length - 1;
            if(originalLength == 0)
            {
                lastSum = numbers[0];
            }
            else
            {
                for (int i = 0; i < originalLength; i++)
                {
                    int[] condensed = new int[numbers.Length - 1];

                    for (int j = 0; j < condensed.Length; j++)
                    {
                        condensed[j] = numbers[j] + numbers[j + 1];

                    }
                    numbers = condensed;
                    lastSum = condensed[0];
                }
            }
            

            Console.WriteLine(lastSum);

        }
    }
}
