using System;

namespace MathOperations
{
    class MathOperations
    {
        static void Main(string[] args)
        {
            int firstValue = int.Parse(Console.ReadLine());
            string operatorSign = Console.ReadLine();
            int secondValue = int.Parse(Console.ReadLine());
            double result = CalculateTwoValues(firstValue, operatorSign, secondValue);
            Console.WriteLine(result);
        }

        static double CalculateTwoValues(int firstValue,
            string operatorSign,
            int secondValue)
        {
            double result = 0;

            switch (operatorSign)
            {
                case "/":
                    result = firstValue / secondValue;
                    break;
                case "*":
                    result = firstValue * secondValue;
                    break;
                case "+":
                    result = firstValue + secondValue;
                    break;
                case "-":
                    result = firstValue - secondValue;
                    break;
            }

            return result;
        }
    }
}
