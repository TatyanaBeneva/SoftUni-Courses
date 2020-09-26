using System;
using System.Linq;

namespace MaxSequenceOfEqualElements
{
    class MaxSequenceOfEqualElements
    {
        static void Main(string[] args)
        {
            int[] numbers = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
            int counter = 1;
            int leftBig = 0;
            int index = 0;

            for(int i = 0; i < numbers.Length; i++)
            {
                if(i == numbers.Length - 1)
                {
                    break;
                }
                else
                {
                    if (numbers[i] == numbers[i + 1])
                    {
                        counter++;
                        if (counter > leftBig)
                        {
                            leftBig = counter;
                            index = numbers[i];
                        }
                    }
                    else
                    {
                        counter = 1;
                    }
                }
            }
            for(int j = 1; j <= leftBig; j++)
            {
                Console.Write($"{index} ");
            }
        }
    }
}
