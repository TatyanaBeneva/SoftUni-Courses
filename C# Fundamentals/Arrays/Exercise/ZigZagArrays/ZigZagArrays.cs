using System;
using System.Linq;
namespace ZigZagArrays
{
    class ZigZagArrays
    {
        static void Main(string[] args)
        {
            int numberOfLines = int.Parse(Console.ReadLine());
            string firstArray = "";
            string secondArray = "";

            for(int i = 0; i < numberOfLines; i++)
            {
                int[] numbers = Console.ReadLine().Split().Select(int.Parse).ToArray();

                if(i % 2 == 0)
                {
                    firstArray += numbers[0] + " ";
                    secondArray += numbers[1] + " ";
                }
                else
                {
                    firstArray += numbers[1] + " ";
                    secondArray += numbers[0] + " ";
                }

            }

            Console.WriteLine(firstArray);
            Console.WriteLine(secondArray);
        }
    }
}
