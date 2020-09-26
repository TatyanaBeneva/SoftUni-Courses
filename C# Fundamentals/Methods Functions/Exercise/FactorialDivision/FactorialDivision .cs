using System;

namespace FactorialDivision
{
    class FactorialDivision
    {
        static void Main(string[] args)
        {
            int firstNumber = Math.Abs(int.Parse(Console.ReadLine()));
            int secondNumber = Math.Abs(int.Parse(Console.ReadLine()));

            ResultOfDividingTheTwoNumbers(firstNumber, secondNumber);
        }

        static double FirstNumberFactorial(int firstNumber)
        {
            double factorialOfFirstNum = firstNumber;
            for(int i = firstNumber - 1; i > 0; i--)
            {
                factorialOfFirstNum *= i;
            }

            return factorialOfFirstNum;
        }

        static double SecondNumberFactorial(int secondNumber)
        {
            double factorialOfSecondNum = secondNumber;
            for (int i = secondNumber - 1; i > 0; i--)
            {
                factorialOfSecondNum *= i;
            }

            return factorialOfSecondNum;
        }

        static void ResultOfDividingTheTwoNumbers(int firstNumber,
            int secondNumber)
        {
            double result = ((double)FirstNumberFactorial(firstNumber) / (double)SecondNumberFactorial(secondNumber));
            Console.WriteLine($"{result:F2}");
        }
    }
}
