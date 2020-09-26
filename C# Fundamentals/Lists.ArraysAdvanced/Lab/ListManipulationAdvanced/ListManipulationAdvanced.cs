using System;
using System.Collections.Generic;
using System.Linq;

namespace ListManipulationAdvanced
{
    class ListManipulationAdvanced
    {
        static void Main(string[] args)
        {
            List<int> numbersOfIntegers = Console.ReadLine().Split(" ").Select(int.Parse).ToList();
            List<int> numbers = numbersOfIntegers;
            string command = Console.ReadLine();
            List<int> result = new List<int>();

            while (command != "end")
            {
                List<string> commands = command.Split(" ").ToList();

                switch (commands[0])
                {
                    case "Contains":
                        ContainsNumber(numbersOfIntegers, commands);
                        break;
                    case "PrintEven":
                        PrintEven(numbersOfIntegers, commands);
                        break;
                    case "PrintOdd":
                        PrintOdd(numbersOfIntegers, commands);
                        break;
                    case "GetSum":
                        GetSumOfAllNumbers(numbersOfIntegers, commands);
                        break;
                    case "Filter":
                        FulfillTheGivenCondition(numbersOfIntegers, commands);
                        break;
                    case "Add":
                        AddNumberToTheEndOfTheList(numbers, commands);
                        break;
                    case "Remove":
                        RemoveNumberFromTheList(numbers, commands);
                        break;
                    case "RemoveAt":
                        RemoveNumberAtGivenIndex(numbers, commands);
                        break;
                    case "Insert":
                        InsertNumberAtGivenIndex(numbers, commands);
                        break;
                }
                if(commands[0] == "Add" || commands[0] == "Remove" || commands[0] == "RemoveAt" || commands[0] == "Insert")
                {
                    result = numbers;
                }

                command = Console.ReadLine();
            }

            if(result == numbers)
            {
                Console.WriteLine(string.Join(" ", numbers));
            }
        }

        static void ContainsNumber(List<int> numbersOfIntegers, List<string> commands)
        {
            int number = int.Parse(commands[1]);
            if (numbersOfIntegers.Contains(number))
            {
                Console.WriteLine("Yes");
            }
            else
            {
                Console.WriteLine("No such number");
            }
        }

        static void PrintEven(List<int> numbersOfIntegers, List<string> commands)
        {
            foreach(int current in numbersOfIntegers)
            {
                if(current % 2 == 0)
                {
                    Console.Write(current + " ");
                }
            }
            Console.WriteLine();
        }

        static void PrintOdd(List<int> numbersOfIntegers, List<string> commands)
        {
            foreach (int current in numbersOfIntegers)
            {
                if (current % 2 != 0)
                {
                    Console.Write(current + " ");
                }
            }
            Console.WriteLine();
        }

        static void GetSumOfAllNumbers(List<int> numbersOfIntegers, List<string> commands)
        {
            int sum = 0;
            foreach (int current in numbersOfIntegers)
            {
                sum += current;
            }
            Console.WriteLine(sum);
        }

        static void FulfillTheGivenCondition(List<int> numbersOfIntegers, List<string> commands)
        {
            int number = int.Parse(commands[2]);

            switch (commands[1])
            {
                case "<":
                    Console.WriteLine(string.Join(" ", numbersOfIntegers.Where(x => x < number)));
                    break;
                case ">":
                    Console.WriteLine(string.Join(" ", numbersOfIntegers.Where(x => x > number)));
                    break;
                case "<=":
                    Console.WriteLine(string.Join(" ", numbersOfIntegers.Where(x => x <= number)));
                    break;
                case ">=":
                    Console.WriteLine(string.Join(" ", numbersOfIntegers.Where(x => x >= number)));
                    break;
            }
        }

        static void AddNumberToTheEndOfTheList(List<int> numbers, List<string> commands)
        {
            int numberToAdd = int.Parse(commands[1]);
            numbers.Add(numberToAdd);
        }

        static void RemoveNumberFromTheList(List<int> numbers, List<string> commands)
        {
            int numberToRemove = int.Parse(commands[1]);
            numbers.Remove(numberToRemove);
        }

        static void RemoveNumberAtGivenIndex(List<int> numbers, List<string> commands)
        {
            int numberToRemoveAtIndex = int.Parse(commands[1]);
            numbers.RemoveAt(numberToRemoveAtIndex);
        }

        static void InsertNumberAtGivenIndex(List<int> numbers, List<string> commands)
        {
            int numberToAddAtIndex = int.Parse(commands[1]);
            int indexToAdd = int.Parse(commands[2]);
            numbers.Insert(indexToAdd, numberToAddAtIndex);
        }
    }
}
