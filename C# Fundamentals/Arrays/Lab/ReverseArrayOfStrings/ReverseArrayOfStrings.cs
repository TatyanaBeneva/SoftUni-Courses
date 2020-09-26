using System;
using System.Linq;

namespace ReverseArrayOfStrings
{
    class ReverseArrayOfStrings
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine();
            string[] splitInput = input.Split(" ");
            Console.WriteLine(string.Join(" ", splitInput.Reverse()));
        }
    }
}
