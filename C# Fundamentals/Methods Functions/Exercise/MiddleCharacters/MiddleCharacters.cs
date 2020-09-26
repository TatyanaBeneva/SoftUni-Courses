using System;

namespace MiddleCharacters
{
    class MiddleCharacters
    {
        static void Main(string[] args)
        {
            string word = Console.ReadLine();
            PrintTheMiddleCharacter(word);
        }

        static void PrintTheMiddleCharacter(string word)
        {
            string result = string.Empty;
            int middleChar = 0;

            if (word.Length % 2 == 0)
            {
                middleChar = word.Length / 2;
                result = $"{word[middleChar - 1]}{word[middleChar]}";
            }
            else
            {
                middleChar = (word.Length + 1) / 2;
                result = $"{word[middleChar - 1]}";
            }

            Console.WriteLine(result);
        }
    }
}
