using System;

namespace DataTypes
{
    class DataTypes
    {
        static void Main(string[] args)
        {
            string dataType = Console.ReadLine();
            var input = Console.ReadLine();

            if(dataType == "int")
            {
                IntegerNumber(int.Parse(input));
            }
            else if(dataType == "real")
            {
                RealNumber(double.Parse(input));
            }
            else if(dataType == "string")
            {
                StringInput(input);
            }
        }

        static void IntegerNumber(int input)
        {
            Console.WriteLine(input * 2);
        }

        static void RealNumber(double input)
        {
            Console.WriteLine($"{(input * 1.5):F2}");
        }

        static void StringInput(string input)
        {
            Console.WriteLine($"${input}$");
        }
    }
}
