using System;

namespace Substring
{
    class Substring
    {
        static void Main(string[] args)
        {
            string word = Console.ReadLine().ToLower();
            string input = Console.ReadLine();

            while (input.Contains(word))
            {
                int indexOfWord = input.IndexOf(word);
                input = input.Remove(indexOfWord, word.Length);
            }

            Console.WriteLine(input);
        }
    }
}
