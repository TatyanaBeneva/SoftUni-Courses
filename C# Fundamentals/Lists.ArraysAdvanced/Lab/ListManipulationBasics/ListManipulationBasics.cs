using System;
using System.Collections.Generic;
using System.Linq;

namespace ListManipulationBasics
{
    class ListManipulationBasics
    {
        static void Main(string[] args)
        {
            List<int> numbers = Console.ReadLine().Split(" ").Select(int.Parse).ToList();
            string command = Console.ReadLine();

            while(command != "end")
            {
                List<string> commands = command.Split(" ").ToList();

                switch (commands[0])
                {
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

                command = Console.ReadLine();
            }

            Console.WriteLine(string.Join(" ", numbers));
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
