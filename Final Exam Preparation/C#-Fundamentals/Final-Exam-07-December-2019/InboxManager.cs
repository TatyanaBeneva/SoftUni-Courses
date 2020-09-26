using System;
using System.Collections.Generic;
using System.Linq;

namespace InboxManager
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, List<string>> namesAndEmails = new Dictionary<string, List<string>>();

            while (true)
            {
                string currentCommand = Console.ReadLine();

                if(currentCommand == "Statistics")
                {
                    Printresult(namesAndEmails);
                    break;
                }
                else
                {
                    string[] command = currentCommand.Split("->");
                    string username = command[1];

                    switch (command[0])
                    {
                        case "Add":
                            AddCommand(namesAndEmails, username);
                            break;
                        case "Send":
                            SendCommand(namesAndEmails, command);
                            break;
                        case "Delete":
                            DeleteCommand(namesAndEmails, username);
                            break;
                    }
                }
            }
        }

        static void Printresult(Dictionary<string, List<string>> namesAndEmails)
        {
            Console.WriteLine($"Users count: {namesAndEmails.Count}");

            foreach(var current in namesAndEmails.OrderByDescending(o => o.Value.Count).ThenBy(n => n.Key))
            {
                Console.WriteLine(current.Key);

                foreach(var emails in current.Value)
                {
                    Console.WriteLine($"- {emails}");
                }
            }
        }

        static void SendCommand(Dictionary<string, List<string>> namesAndEmails,
            string[] command)
        {
            string username = command[1];
            string email = command[2];
            namesAndEmails[username].Add(email);
        }

        static void DeleteCommand(Dictionary<string, List<string>> namesAndEmails,
            string username)
        {
            if(IsUsernameExist(namesAndEmails, username) == true)
            {
                namesAndEmails.Remove(username);
            }
            else
            {
                Console.WriteLine($"{username} not found!");
            }
        }

        static void AddCommand(Dictionary<string, List<string>> namesAndEmails,
            string username)
        {
            if(IsUsernameExist(namesAndEmails, username) == true)
            {
                Console.WriteLine($"{username} is already registered");
            }
            else
            {
                namesAndEmails.Add(username, new List<string> { });
            }
        }

        static bool IsUsernameExist(Dictionary<string, List<string>> namesAndEmails,
            string username)
        {
            if (namesAndEmails.ContainsKey(username))
            {
                return true;
            }

            return false;
        }
    }
}
