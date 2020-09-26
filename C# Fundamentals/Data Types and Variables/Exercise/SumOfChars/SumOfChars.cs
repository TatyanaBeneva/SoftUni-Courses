using System;

namespace SumOfChars
{
    class SumOfChars
    {
        static void Main(string[] args)
        {
            int numberOfLines = int.Parse(Console.ReadLine());
            int sumOfChar = 0;

            for(int i = 1; i <= numberOfLines; i++)
            {
                char simbol = char.Parse(Console.ReadLine());
                int numOfChar = (char)simbol;
                sumOfChar += numOfChar;
            }

            Console.WriteLine($"The sum equals: {sumOfChar}");
        }
    }
}
