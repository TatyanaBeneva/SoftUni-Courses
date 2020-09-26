using System;

namespace DataTypeFinder
{
    class DataTypeFinder
    {
        static void Main(string[] args)
        {
            var command = Console.ReadLine();

            while(command != "END")
            {
                var integer = command;
                if(int.TryParse(integer, out int number))
                {
                    Console.WriteLine($"{integer} is integer type");
                }
                else if(double.TryParse(integer, out double floatingNumber))
                {
                    Console.WriteLine($"{integer} is floating point type");
                }
                else if(char.TryParse(integer, out char symbol))
                {
                    Console.WriteLine($"{integer} is character type");
                }
                else if(bool.TryParse(integer, out bool check))
                {
                    Console.WriteLine($"{integer} is boolean type");
                }
                else
                {
                    Console.WriteLine($"{integer} is string type");
                }

                
                command = Console.ReadLine();
            }
        }
    }
}
