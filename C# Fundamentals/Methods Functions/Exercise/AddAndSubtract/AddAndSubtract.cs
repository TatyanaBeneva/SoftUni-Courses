using System;

namespace AddAndSubtract
{
    class AddAndSubtract
    {
        static void Main(string[] args)
        {
            int firstValue = int.Parse(Console.ReadLine());
            int secondValue = int.Parse(Console.ReadLine());
            int thirdValue = int.Parse(Console.ReadLine());

            SubstractTheThirdNumberFromTheSumOfFirstTwoNumbers(firstValue, secondValue, thirdValue);
        }

        static int SumFromFirstTwoNumbers(int firstValue,
            int secondValue)
        {
            return firstValue + secondValue;
        }

        static void SubstractTheThirdNumberFromTheSumOfFirstTwoNumbers(int firstValue,
            int secondValue, 
            int thirdValue)
        {
            int result = SumFromFirstTwoNumbers(firstValue, secondValue) - thirdValue;
            Console.WriteLine(result);
        }
    }
}
