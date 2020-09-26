using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SoftUniParking
{
    class SoftUniParking
    {
        static void Main(string[] args)
        {
            int numOfLines = int.Parse(Console.ReadLine());
            var parkingSpots = new Dictionary<string, string>();

            for(int i = 0; i < numOfLines; i++)
            {
                string[] command = Console.ReadLine().Split(" ");

                switch (command[0])
                {
                    case "register":
                        RegisterCommand(parkingSpots, command);
                        break;
                    default:
                        UnregisterCommand(parkingSpots, command);
                        break;
                }
            }

            foreach(var name in parkingSpots)
            {
                Console.WriteLine($"{name.Key} => {name.Value}");
            }
        }

        static void RegisterCommand(Dictionary<string, string> parkingSpots, string[] command)
        {
            if(IsNameExist(parkingSpots, command) == true)
            {
                Console.WriteLine($"ERROR: already registered with plate number {parkingSpots[command[1]]}");
            }
            else
            {
                parkingSpots.Add(command[1], command[2]);
                Console.WriteLine($"{command[1]} registered {command[2]} successfully");
            }
        }

        static void UnregisterCommand(Dictionary<string, string> parkingSpots, string[] command)
        {
            if(IsNameExist(parkingSpots, command) == false)
            {
                Console.WriteLine($"ERROR: user {command[1]} not found");
            }
            else
            {
                parkingSpots.Remove(command[1]);
                Console.WriteLine($"{command[1]} unregistered successfully");
            }
        }

        static bool IsNameExist(Dictionary<string, string> parkingSpots, string[] command)
        {
            if (parkingSpots.ContainsKey(command[1]))
            {
                return true;
            }

            return false;
        }
    }
}
