using System;
using System.Collections.Generic;
using System.Linq;

namespace ChangeList
{
    class ChangeList
    {
        static void Main(string[] args)
        {
            List<int> numbers = Console.ReadLine().Split(" ").Select(int.Parse).ToList();
            string endCommand = Console.ReadLine();

            while(endCommand != "end")
            {
                List<string> commands = endCommand.Split(" ").ToList();
                switch (commands[0])
                {
                    case "Delete":
                        DeleteElements(numbers, commands);
                        break;
                    case "Insert":
                        InsertNumber(numbers, commands);
                        break;
                }
                endCommand = Console.ReadLine();
            }

            Console.WriteLine(string.Join(" ", numbers));
        }

        static void DeleteElements(List<int> numbers, List<string> commands)
        {
            int deleteNumber = int.Parse(commands[1]);
            for(int i = 0; i < numbers.Count; i++)
            {
                numbers.Remove(deleteNumber);
            }
        }

        static void InsertNumber(List<int> numbers, List<string> commands)
        {
            int elementNumber = int.Parse(commands[1]);
            int index = int.Parse(commands[2]);
            numbers.Insert(index, elementNumber);
        }
    }
}
