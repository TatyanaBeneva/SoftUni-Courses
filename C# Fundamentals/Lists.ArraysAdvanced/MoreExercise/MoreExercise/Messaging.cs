using System;
using System.Linq;
using System.Collections.Generic;

namespace Messaging
{
    class Messaging
    {
        static void Main(string[] args)
        {
            List<string> numbers = Console.ReadLine().Split(" ").ToList();
            string word = Console.ReadLine();

            SumEveryIndex(numbers, word);
        }

        static void SumEveryIndex(List<string> numbers, string word)
        {
            string result = string.Empty;
            for(int i = 0; i < numbers.Count; i++)
            {
                int sum = 0;
                int currentNumLenght = numbers[i].Length;
                int currentIndex = int.Parse(numbers[i]);
                for (int j = 0; j < currentNumLenght; j++)
                {                    
                    int currentNum = currentIndex % 10;
                    sum += currentNum;
                    currentIndex = currentIndex / 10;
                }
                int index = (sum) % (word.Length);
                result += word[index];
                word = word.Remove(index, 1);
            }
            Console.WriteLine(result);
        }
    }
}
