using System;

namespace RepeateStrings
{
    class RepeateStrings
    {
        static void Main(string[] args)
        {
            string[] inputArray = Console.ReadLine().Split();
            string result = string.Empty;

            foreach(var currentWord in inputArray)
            {
                for(int i = 0; i < currentWord.Length; i++)
                {
                    result += currentWord;
                }
            }

            Console.WriteLine(result);
        }
    }
}
