using System;
using System.Collections.Generic;
using System.Linq;

namespace MessagesManager
{
    class MessagesManager
    {
        static void Main(string[] args)
        {
            int capacityPerUser = int.Parse(Console.ReadLine());
            Dictionary<string, int> nameAndSentinformation = new Dictionary<string, int>();

            while (true)
            {
                string command = Console.ReadLine();

                if(command == "Statistics")
                {
                    PrintTheResult(nameAndSentinformation);
                    break;
                }
                else
                {
                    string[] currentCommand = command.Split("=");

                    switch (currentCommand[0])
                    {
                        case "Add":
                            AddCommand(nameAndSentinformation, currentCommand);
                            break;
                        case "Message":
                            MessageCommand(nameAndSentinformation, currentCommand, capacityPerUser);
                            break;
                        case "Empty":
                            EmptyCommand(nameAndSentinformation, currentCommand);
                            break;
                    }
                }
            }

            
        }

        static void PrintTheResult(Dictionary<string, int> nameAndSentinformation)
        {
            nameAndSentinformation = nameAndSentinformation.OrderBy(o => o.Key).ThenByDescending(t => t.Value)
                .ToDictionary(k => k.Key, k => k.Value);

            Console.WriteLine($"Users count: {nameAndSentinformation.Count}");

            foreach(var current in nameAndSentinformation)
            {
                Console.WriteLine($"{current.Key} - {current.Value}");
            }
        }

        static void EmptyCommand(Dictionary<string, int> nameAndSentinformation,
            string[] currentCommand)
        {
            string name = currentCommand[1];

            if(IsNameExistAddCommand(nameAndSentinformation, name) == true)
            {
                nameAndSentinformation.Remove(name);
            }
            else if(name == "All")
            {
                nameAndSentinformation.Clear();
            }
        }

        static void MessageCommand(Dictionary<string, int> nameAndSentinformation,
            string[] currentCommand,
            int capacityPerUser)
        {
            string sender = currentCommand[1];
            string receiver = currentCommand[2];

            if(IsSenderAndReceiverExist(nameAndSentinformation, sender, receiver) == true)
            {
                nameAndSentinformation[sender]++;
                nameAndSentinformation[receiver]++;

                if(nameAndSentinformation[sender] >= capacityPerUser)
                {
                    Console.WriteLine($"{sender} reached the capacity!");
                    nameAndSentinformation.Remove(sender);
                }

                if(nameAndSentinformation[receiver] >= capacityPerUser)
                {
                    Console.WriteLine($"{receiver} reached the capacity!");
                    nameAndSentinformation.Remove(receiver);
                }
            }
        }

        static bool IsSenderAndReceiverExist(Dictionary<string, int> nameAndSentinformation,
            string sender,
            string receiver)
        {
            if(nameAndSentinformation.ContainsKey(sender) && nameAndSentinformation.ContainsKey(receiver))
            {
                return true;
            }

            return false;
        }

        static void AddCommand(Dictionary<string, int> nameAndSentinformation,
            string[] currentCommand)
        {
            string name = currentCommand[1];
            int sent = int.Parse(currentCommand[2]);
            int received = int.Parse(currentCommand[3]);
            int sum = sent + received;

            if(IsNameExistAddCommand(nameAndSentinformation, name) == false)
            {
                nameAndSentinformation.Add(name, sum);
            }
        }

        static bool IsNameExistAddCommand(Dictionary<string, int> nameAndSentinformation,
            string name)
        {
            if(nameAndSentinformation.ContainsKey(name))
            {
                return true;
            }

            return false;
        }
    }
}
