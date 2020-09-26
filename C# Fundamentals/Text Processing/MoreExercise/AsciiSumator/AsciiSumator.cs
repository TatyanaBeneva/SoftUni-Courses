using System;

namespace AsciiSumator
{
    class AsciiSumator
    {
        static void Main(string[] args)
        {
            char firstChar = char.Parse(Console.ReadLine());
            char secondChar = char.Parse(Console.ReadLine());
            string text = Console.ReadLine();
            int sum = 0;

            foreach(char current in text)
            {
                if(current > firstChar && current < secondChar)
                {
                    sum += current;
                }
            }

            Console.WriteLine(sum);
        }
    }
}
