using System;
using System.Numerics;

namespace BigFactorial
{
    class BigFactorial
    {
        static void Main(string[] args)
        {
            int number = int.Parse(Console.ReadLine());
            BigInteger largerInteger = 1;
            for(int i = 2; i <= number; i++)
            {
                largerInteger *= i;
            }

            Console.WriteLine(largerInteger);
        }
    }
}
