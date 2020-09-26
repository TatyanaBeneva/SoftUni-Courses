using System;

namespace SumDigits
{
    class SumDigits
    {
        static void Main(string[] args)
        {
            int number = int.Parse(Console.ReadLine());

            int currentNumber = 0;
            int sum = 0;

            while (number != 0)
            {
                currentNumber = number % 10;
                number = number / 10;
                sum += currentNumber;
            }

            Console.WriteLine(sum);
        }
    }
}
