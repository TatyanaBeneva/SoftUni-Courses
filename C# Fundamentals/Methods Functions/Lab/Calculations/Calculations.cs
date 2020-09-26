using System;

namespace Calculations
{
    class Calculations
    {
        static void Main(string[] args)
        {
            string operation = Console.ReadLine();
            double firstNumber = double.Parse(Console.ReadLine());
            double secondNumber = double.Parse(Console.ReadLine());

            switch (operation)
            {
                case "add":
                    AddTwoNumbers(firstNumber, secondNumber);
                    break;
                case "multiply":
                    MultiplyTwoNumbers(firstNumber, secondNumber);
                    break;
                case "subtract":
                    SubtractTwoNumbers(firstNumber, secondNumber);
                    break;
                case "divide":
                    DivideTwoNumbers(firstNumber, secondNumber);
                    break;
            }
        }

        static void AddTwoNumbers(double firtsNumber,
            double secondNumber)
        {
            Console.WriteLine(firtsNumber + secondNumber);
        }

        static void MultiplyTwoNumbers(double firtsNumber,
            double secondNumber)
        {
            Console.WriteLine(firtsNumber * secondNumber);
        }

        static void SubtractTwoNumbers(double firtsNumber,
            double secondNumber)
        {
            Console.WriteLine(firtsNumber - secondNumber);
        }

        static void DivideTwoNumbers(double firtsNumber,
            double secondNumber)
        {
            Console.WriteLine(firtsNumber / secondNumber);
        }
    }
}
