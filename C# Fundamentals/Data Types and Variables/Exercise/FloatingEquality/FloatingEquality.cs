using System;

namespace FloatingEquality
{
    class FloatingEquality
    {
        static void Main(string[] args)
        {
            decimal firstNumber = decimal.Parse(Console.ReadLine());
            decimal secondNumber = decimal.Parse(Console.ReadLine());
            bool equal = Math.Abs(firstNumber - secondNumber) < 0.000001m;
            Console.WriteLine(equal);
        }
    }
}
