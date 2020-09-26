using System;
using System.Collections.Generic;
using System.Linq;

namespace Train
{
    class Train
    {
        static void Main(string[] args)
        {
            List<int> personOfEveryVagon = Console.ReadLine().Split(" ").Select(int.Parse).ToList();
            int capacityOfVagons = int.Parse(Console.ReadLine());
            string command = Console.ReadLine();
            int index = 0;

            while (command != "end")
            {
                List<string> input = command.Split(" ").ToList();
                switch (input[0])
                {
                    case "Add":
                        AddPassengers(personOfEveryVagon, input);
                        break;
                    default:
                        FitEveryPassengers(personOfEveryVagon, input, capacityOfVagons, index);
                        break;
                }

                command = Console.ReadLine();
            }

            Console.WriteLine(string.Join(" ", personOfEveryVagon));
        }

        static void AddPassengers(List<int> personOfEveryVagon, List<string> input)
        {
            int number = int.Parse(input[1]);
            personOfEveryVagon.Add(number);
        }

        static void FitEveryPassengers(List<int> personOfEveryVagon, List<string> input, int capacityOfVagons, int index)
        {
            int passengers = int.Parse(input[0]);
            for(int i = 0; i < personOfEveryVagon.Count; i++)
            {
                int sumOfBeforeAndNext = personOfEveryVagon[index] + passengers;
                if (sumOfBeforeAndNext > capacityOfVagons)
                {
                    index++;
                    continue;
                }
                else
                {
                    personOfEveryVagon[index] = sumOfBeforeAndNext;
                    break;
                }
            }
        }
    }
}
