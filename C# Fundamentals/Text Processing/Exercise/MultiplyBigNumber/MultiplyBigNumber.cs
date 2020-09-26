using System;
using System.Numerics;

namespace MultiplyBigNumber
{
    class MultiplyBigNumber
    {
        static void Main(string[] args)
        {
            BigInteger firstNum = BigInteger.Parse(Console.ReadLine());
            sbyte secondNum = sbyte.Parse(Console.ReadLine());
            Console.WriteLine(firstNum * secondNum);
        }
    }
}
