using System;
using System.Linq;

namespace MultiplyEvensByOdds
{
    class MultiplyEvensByOdds
    {
        static void Main(string[] args)
        {
            int number = Math.Abs(int.Parse(Console.ReadLine()));
            Console.WriteLine(GetMultipleOfEvenAndOdds(GetSumOfEvenDigits(number),
                GetSumOfOddDigits(number)));
        }

        private static int GetSumOfEvenDigits(int number)
        {
            int currDigit = 0;
            int sum = 0;
            while (number > 0)
            {
                currDigit = number % 10;

                if (currDigit % 2 == 0)
                    sum = sum + currDigit;

                number = number / 10;
            }
            return sum;
        }

        private static int GetSumOfOddDigits(int number)
        {
            int currDigit = 0;
            int sum = 0;
            while (number > 0)
            {
                currDigit = number % 10;

                if (currDigit % 2 == 1)
                    sum = sum + currDigit;

                number = number / 10;
            }
            return sum;
        }

        private static int GetMultipleOfEvenAndOdds(int evenSum, int oddSum)
        {
            return evenSum * oddSum;
        }
    }
}
