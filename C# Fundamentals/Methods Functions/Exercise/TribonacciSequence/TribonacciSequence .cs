using System;

namespace TribonacciSequence
{
    class TribonacciSequence
    {
        static void Main(string[] args)
        {
            int numOfNumbers = int.Parse(Console.ReadLine());
            TribonacciiLine(numOfNumbers);
        }

        static void TribonacciiLine(int numOfNumbers)
        {
            int[] result = new int[numOfNumbers];
            for(int i = 0; i < numOfNumbers; i++)
            {
                if(i == 0)
                {
                    result[i] = 1;
                }
                else if(i == 1)
                {
                    result[i] = 1;
                }
                else if(i == 2)
                {
                    result[i] = 2;
                }
                else if(i > 2)
                {
                    result[i] = result[i - 1] + result[i - 2] + result[i - 3];
                }
            }

            Console.WriteLine(string.Join(" ", result));
        }
    }
}
