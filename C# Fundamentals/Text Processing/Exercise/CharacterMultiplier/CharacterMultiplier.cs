using System;

namespace CharacterMultiplier
{
    class CharacterMultiplier
    {
        static void Main(string[] args)
        {
            string[] input = Console.ReadLine().Split(" ");

            Console.WriteLine(SumOfChars(input));
        }

        static int SumOfChars(string[] input)
        {
            string firstWord = input[0];
            string secondWord = input[1];

            int sum = 0;

            if(firstWord.Length == secondWord.Length)
            {
                for(int i = 0; i < firstWord.Length; i++)
                {
                    sum += (firstWord[i] * secondWord[i]);
                }
            }
            else
            {
                if(firstWord.Length > secondWord.Length)
                {
                    for(int i = 0; i < secondWord.Length; i++)
                    {
                        sum += (firstWord[i] * secondWord[i]);
                    }

                    for(int i = secondWord.Length; i < firstWord.Length; i++)
                    {
                        sum += firstWord[i];
                    }
                }
                else
                {
                    for (int i = 0; i < firstWord.Length; i++)
                    {
                        sum += (firstWord[i] * secondWord[i]);
                    }

                    for (int i = firstWord.Length; i < secondWord.Length; i++)
                    {
                        sum += secondWord[i];
                    }
                }
            }

            return sum;
        }
    }
}
