using System;

namespace SpecialNumbers
{
    class SpecialNumbers
    {
        static void Main(string[] args)
        {
            int num = int.Parse(Console.ReadLine());

                for (int i = 1; i <= num; i++)
                {
                    int sumOfDigit = 0;
                    int digit = i;

                    while (digit > 0)
                    {
                        sumOfDigit += digit % 10;
                        digit = digit / 10;                       
                    }

                switch (sumOfDigit)
                {
                    case 5:
                    case 7:
                    case 11:
                        Console.WriteLine($"{i} -> True");
                        break;
                    default:
                        Console.WriteLine($"{i} -> False");
                        break;
                }
            }
        }
    }
}
