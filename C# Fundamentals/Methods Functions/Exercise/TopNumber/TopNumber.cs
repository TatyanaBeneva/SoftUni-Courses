using System;

namespace TopNumber
{
    class TopNumber
    {
        static void Main(string[] args)
        {
            int number = int.Parse(Console.ReadLine());
            IfSumOfDiggitsIsDivisbleBy8(number);
        }

        static void IfSumOfDiggitsIsDivisbleBy8(int number)
        {
            for(int i = 1; i <= number; i++)
            {
                int topNumber = 0;
                int currentNum = i;
                int sumOfDiggits = 0;
                string length = $"{i}";
                for(int j = 1; j <= length.Length; j++)
                {
                    int numberOdd = currentNum % 10;
                    if (numberOdd % 2 != 0)
                    {
                        topNumber = i;
                    }
                    sumOfDiggits += currentNum % 10;
                    currentNum /= 10;
                }
                if(sumOfDiggits % 8 == 0 && topNumber == i)
                {
                    Console.WriteLine(topNumber);
                }
            }
        }
    }
}
