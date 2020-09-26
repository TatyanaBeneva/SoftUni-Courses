using System;

namespace TriplesOfLatinLetters
{
    class TriplesOfLatinLetters
    {
        static void Main(string[] args)
        {
            int number = int.Parse(Console.ReadLine());

            for(int i = 0; i < number; i++)
            {
                char firstChar = Convert.ToChar(97 + i);
                for(int j = 0; j < number; j++)
                {
                    char secondChar = Convert.ToChar(97 + j);
                    for (int k = 0; k < number; k++)
                    {
                        char thirdChar = Convert.ToChar(97 + k);
                        Console.WriteLine($"{firstChar}{secondChar}{thirdChar}");
                    }
                }
            }
        }
    }
}
