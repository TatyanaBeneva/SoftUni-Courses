using System;
using System.Linq;
using System.Collections.Generic;

namespace CarRace
{
    class CarRace
    {
        static void Main(string[] args)
        {
            List<int> numbers = Console.ReadLine().Split(" ").Select(int.Parse).ToList();
            LetsSeeWhoWillWin(numbers);
        }

        static void LetsSeeWhoWillWin(List<int> numbers)
        {
            int numberOfTimesOfEachPlayer = numbers.Count / 2;
            double leftPlayerTime = 0;
            double rightPlayerTime = 0;
            double timeBeforeZero = 0;
            for (int i = 0; i < numberOfTimesOfEachPlayer; i++)
            {
                if (numbers[i] != 0)
                {
                    timeBeforeZero += numbers[i];
                }
                else
                {
                    leftPlayerTime += (timeBeforeZero * 0.8);
                    timeBeforeZero = 0;
                }
            }
            leftPlayerTime += timeBeforeZero;
            timeBeforeZero = 0;
            for (int i = numbers.Count - 1; i > numberOfTimesOfEachPlayer; i--)
            {
                if (numbers[i] != 0)
                {
                    timeBeforeZero += numbers[i];
                }
                else
                {
                    rightPlayerTime += (timeBeforeZero * 0.8);
                    timeBeforeZero = 0;
                }
            }
            rightPlayerTime += timeBeforeZero;

            if (leftPlayerTime < rightPlayerTime)
            {
                Console.WriteLine($"The winner is left with total time: {leftPlayerTime}");
            }
            else
            {
                Console.WriteLine($"The winner is right with total time: {rightPlayerTime}");
            }
        }
    }
}
