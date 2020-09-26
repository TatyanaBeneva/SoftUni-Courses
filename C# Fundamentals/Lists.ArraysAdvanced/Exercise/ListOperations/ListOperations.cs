using System;
using System.Collections.Generic;
using System.Linq;

namespace ListOperations
{
    class ListOperations
    {
        static void Main(string[] args)
        {
            List<int> numbers = Console.ReadLine().Split(" ").Select(int.Parse).ToList();
            string commands = Console.ReadLine();

            while(commands != "End")
            {
                List<string> givenCommand = commands.Split(" ").ToList();
                switch (givenCommand[0])
                {
                    case "Add":
                        int number = int.Parse(givenCommand[1]);
                        numbers.Add(number);
                        break;
                    case "Insert":
                        int index = int.Parse(givenCommand[2]);
                        if (index > (numbers.Count - 1) || index < 0)
                        {
                            Console.WriteLine("Invalid index");
                        }
                        else
                        {
                            number = int.Parse(givenCommand[1]);
                            numbers.Insert(index, number);
                        }
                        break;
                    case "Remove":
                        number = int.Parse(givenCommand[1]);
                        if (number > (numbers.Count - 1) || number < 0)
                        {
                            Console.WriteLine("Invalid index");
                        }
                        else
                        {
                            numbers.RemoveAt(number);
                        }
                        break;
                    case "Shift":
                        if(givenCommand[1] == "left")
                        {
                            ShiftLeft(numbers, givenCommand);
                        }
                        else
                        {
                            ShiftRight(numbers, givenCommand);
                        }
                        break;
                }

                commands = Console.ReadLine();
            }

            Console.WriteLine(string.Join(" ", numbers));
        }

        static void ShiftLeft(List<int> numbers, List<string> givenCommand)
        {
            int index = int.Parse(givenCommand[2]);
            for (int i = 0; i < index; i++)
            {
                int firstNum = numbers[0];
                numbers.Add(firstNum);
                numbers.Remove(firstNum);
            }
        }

        static void ShiftRight(List<int> numbers, List<string> givenCommand)
        {
            int index = int.Parse(givenCommand[2]);
            for (int i = 0; i < index; i++)
            {
                int lastNum = numbers[numbers.Count - 1];
                numbers.Insert(0, lastNum);
                numbers.RemoveAt(numbers.Count - 1);
            }
        }
    }
}
