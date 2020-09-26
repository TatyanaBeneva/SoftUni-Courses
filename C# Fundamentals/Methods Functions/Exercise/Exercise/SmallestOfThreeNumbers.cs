using System;

namespace SmallestOfThreeNumbers
{
    class SmallestOfThreeNumbers
    {
        static void Main(string[] args)
        {
            int firstNum = int.Parse(Console.ReadLine());
            int secondNum = int.Parse(Console.ReadLine());
            int thirdNum = int.Parse(Console.ReadLine());

            PrintSmallestNumber(firstNum, secondNum, thirdNum);
        }

        static void PrintSmallestNumber(int firstNum, int secondNum, int thirdNum)
        {
            int smallestNum = 0;
            if (firstNum <= secondNum && firstNum <= thirdNum)
            {
                smallestNum = firstNum;
            }
            else if (secondNum <= firstNum && secondNum <= thirdNum)
            {
                smallestNum = secondNum;
            }
            else if (thirdNum <= firstNum && thirdNum <= secondNum)
            {
                smallestNum = thirdNum;
            }

            Console.WriteLine(smallestNum);
        }
    }
}
