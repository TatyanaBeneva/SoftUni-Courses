using System;

namespace PrintPartOfTheASCIITable
{
    class PrintPartOfTheASCIITable
    {
        static void Main(string[] args)
        {
            int firstChar = int.Parse(Console.ReadLine());
            int secondChar = int.Parse(Console.ReadLine());
            string result = "";

            for(int i = firstChar; i <= secondChar; i++)
            {
                char simbol = Convert.ToChar(i);
                result += simbol + " ";
            }

            Console.WriteLine(result);
        }
    }
}
