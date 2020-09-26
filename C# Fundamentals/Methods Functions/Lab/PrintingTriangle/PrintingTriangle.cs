using System;
using System.Linq;

namespace PrintingTriangle
{
    class PrintingTriangle
    {
        static void Main(string[] args)
        {
            int readValueFromConsole = int.Parse(Console.ReadLine());

            PrintTriangle(readValueFromConsole);
        }

        static void PrintTriangle(int passedValue)
        {
            string result = string.Empty;

            for(int i = 1; i < passedValue + 1; i++)
            {
                for(int y = 1; y <= i; y++)
                {
                    Console.Write(y + " ");                   
                }
                Console.WriteLine();
            }
            for (int i = passedValue - 1; i >= 1; i--)
            {
                for (int y = 1; y <= i; y++)
                {
                    Console.Write(y + " ");
                }
                Console.WriteLine();
            }

        }
    }
}
