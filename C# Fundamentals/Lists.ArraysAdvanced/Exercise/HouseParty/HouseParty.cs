using System;
using System.Collections.Generic;
using System.Linq;

namespace HouseParty
{
    class HouseParty
    {
        static void Main(string[] args)
        {
            int numberOfCommands = int.Parse(Console.ReadLine());
            List<string> guestsGoing = new List<string>();
            List<string> guestsNotGoing = new List<string>();
            for (int i = 0; i < numberOfCommands; i++)
            {
                List<string> commands = Console.ReadLine().Split(" ").ToList();
                switch (commands.Count)
                {
                    case 3:
                        TheyGoingToTheParty(commands, guestsGoing, guestsNotGoing);
                        break;
                    default:
                        TheyDoNotGoToTheParty(commands, guestsNotGoing, guestsGoing);
                        break;
                }
            }

            Console.WriteLine(string.Join("\n", guestsNotGoing));
            Console.WriteLine(string.Join("\n", guestsGoing));
        }

        static void TheyGoingToTheParty(List<string> commands, List<string> guestsGoing, List<string> guestsNotGoing)
        {
            if (guestsGoing.Contains(commands[0]))
            {
                guestsNotGoing.Add(commands[0] + " is already in the list!");
            }
            else
            {
                guestsGoing.Add(commands[0]);
            }          
        }

        static void TheyDoNotGoToTheParty(List<string> commands, List<string> guestsNotGoing, List<string> guestsGoing)
        {
            if (guestsGoing.Contains(commands[0]))
            {
                guestsGoing.Remove(commands[0]);
            }
            else
            {
                guestsNotGoing.Add(commands[0] + " is not in the list!");
            }           
        }
    }
}
