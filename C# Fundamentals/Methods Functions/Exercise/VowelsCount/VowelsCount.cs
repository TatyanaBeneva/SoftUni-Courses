using System;

namespace VowelsCount
{
    class VowelsCount
    {
        static void Main(string[] args)
        {
            string word = Console.ReadLine();
            PrintVowelsInWord(word);
        }

        static void PrintVowelsInWord(string word)
        {
            int countOfVowels = 0;
            for(int i = 0; i < word.Length; i++)
            {
                switch (word[i])
                {
                    case 'a':
                        countOfVowels++;
                        break;
                    case 'A':
                        countOfVowels++;
                        break;
                    case 'i':
                        countOfVowels++;
                        break;
                    case 'I':
                        countOfVowels++;
                        break;
                    case 'e':
                        countOfVowels++;
                        break;
                    case 'E':
                        countOfVowels++;
                        break;
                    case 'o':
                        countOfVowels++;
                        break;
                    case 'O':
                        countOfVowels++;
                        break;
                    case 'u':
                        countOfVowels++;
                        break;
                    case 'U':
                        countOfVowels++;
                        break;
                }
            }
            Console.WriteLine(countOfVowels);
        }
    }
}
