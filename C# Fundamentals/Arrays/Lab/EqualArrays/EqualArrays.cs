using System;
using System.Linq;
namespace EqualArrays
{
    class EqualArrays
    {
        static void Main(string[] args)
        {
            int[] firstArray = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int[] secondtArray = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int sum = 0;
            int sumOfIdentical = 0;
            
            for(int i = 0; i < firstArray.Length; i++)
            {
                sumOfIdentical += firstArray[i];

                if(firstArray[i] != secondtArray[i])
                {
                    Console.WriteLine($"Arrays are not identical. Found difference at {i} index");
                    break;
                }
                else
                {
                    sum += firstArray[i];
                }
            }

            if(sum == sumOfIdentical)
            {
                Console.WriteLine($"Arrays are identical. Sum: {sum}");
            }
        }
    }
}
