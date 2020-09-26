using System;

namespace ExtractPersonInformation
{
    class ExtractPersonInformation
    {
        static void Main(string[] args)
        {
            int numOfLines = int.Parse(Console.ReadLine());

            for(int i = 0; i < numOfLines; i++)
            {
                string text = Console.ReadLine();
                int indexOfFirstCharName = text.IndexOf('@');
                int indexOfLastCharName = text.IndexOf('|');
                string name = text.Substring(indexOfFirstCharName + 1, indexOfLastCharName - indexOfFirstCharName - 1);
                int indexOfFirstCharAge = text.IndexOf('#');
                int indexOfLastCharAge = text.IndexOf('*');
                string age = text.Substring(indexOfFirstCharAge + 1, indexOfLastCharAge - indexOfFirstCharAge - 1);

                Console.WriteLine($"{name} is {age} years old.");
            }
        }
    }
}
