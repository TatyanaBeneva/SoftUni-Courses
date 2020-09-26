using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ReverseStrings
{
    class ReverseStrings
    {
        static void Main(string[] args)
        {
            while (true)
            {
                string command = Console.ReadLine();

                if(command == "end")
                {
                    break;
                }

                List<char> listOfChars = command.ToList();
                listOfChars.Reverse();
                Console.WriteLine($"{command} = {string.Join("", listOfChars)}");
            }
        }
    }
}
