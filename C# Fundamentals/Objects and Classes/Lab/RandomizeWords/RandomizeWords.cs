using System;
using System.Collections.Generic;

namespace RandomizeWords
{
    class RandomizeWords
    {
        static void Main(string[] args)
        {
            string words = Console.ReadLine();
            string[] wordsArray = words.Split(" ");
            List<string> wordsList = new List<string>();
            wordsList.AddRange(wordsArray);
            Shiffle(wordsList);
            Console.WriteLine(string.Join("\n", wordsList));

        }

        static void Shiffle(List<string> wordsList)
        {
            Random rnd = new Random();
            int listCount = wordsList.Count;
            while (listCount > 1)
            {
                listCount--;
                int randomPosition = rnd.Next(listCount + 1);
                string valueOfRandomElement = wordsList[randomPosition];
                wordsList[randomPosition] = wordsList[listCount];
                wordsList[listCount] = valueOfRandomElement;
            }
        }
    }
}
