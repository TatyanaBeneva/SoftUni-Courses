using System;

namespace CharactersInRange
{
    class CharactersInRange
    {
        static void Main(string[] args)
        {
            char firtsChar = char.Parse(Console.ReadLine());
            char secondChar = char.Parse(Console.ReadLine());
            PrintCharsBetweenTwoChars(firtsChar, secondChar);
        }

        static void PrintCharsBetweenTwoChars(char firstChar,
            char secondChar)
        {
            if(firstChar < secondChar)
            {
                for (int i = firstChar + 1; i < secondChar; i++)
                {
                    char curremntChar = (char)i;
                    Console.Write(curremntChar + " ");
                }
            }
            else
            {
                for (int i = secondChar + 1; i < firstChar; i++)
                {
                    char curremntChar = (char)i;
                    Console.Write(curremntChar + " ");
                }
            }
        }
    }
}
