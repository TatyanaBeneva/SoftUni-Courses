using System;
using System.Linq;
namespace EqualSums
{
    class EqualSums
    {
        static void Main(string[] args)
        {
            int[] numbers = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();

            for (int i = 0; i < numbers.Length; i++)
            {
                int leftSum = 0;
                int rightSum = 0;

                for (int j = 0; j < i; j++)
                {
                    leftSum += numbers[j];
                }

                for (int k = i + 1; k < numbers.Length; k++)
                {
                    rightSum += numbers[k];
                }

                if (rightSum == leftSum)
                {
                    Console.WriteLine(i);
                    if (numbers[i] == 0 && numbers[i + 1] == 0)
                    {
                        continue;
                    }
                    else
                    {
                        return;
                    }
                }
                else if(i == numbers.Length - 1)
                {
                    Console.WriteLine("no");
                }
            }
        }
    }
}
