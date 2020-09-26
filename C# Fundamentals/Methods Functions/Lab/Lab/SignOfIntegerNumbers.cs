using System;

namespace SignOfIntegerNumbers
{
    class SignOfIntegerNumbers
    {
        static void Main(string[] args)
        {
            var readValueFromConsole = Console.ReadLine();

            int inputValue = int.Parse(readValueFromConsole);
            PrintSignValue(inputValue);
        }

        static void PrintSignValue(int number)
        {
            if(number > 0)
            {
                Console.WriteLine($"The number {number} is positive.");
            }
            else if(number < 0)
            {
                Console.WriteLine($"The number {number} is negative.");
            }
            else
            {
                Console.WriteLine($"The number {number} is zero.");
            }
        }
    }
}
