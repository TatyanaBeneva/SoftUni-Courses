using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ForceBook
{
    class ForceBook
    {
        static void Main(string[] args)
        {
            var forceBook = new Dictionary<string, List<string>>();

            while (true)
            {
                string command = Console.ReadLine();

                if(command == "Lumpawaroo")
                {
                    forceBook = forceBook.OrderByDescending(o => o.Value.Count)
                        .ThenBy(o => o.Key)
                        .ToDictionary(k => k.Key, v => v.Value);
                    PrintResult(forceBook);
                    break;
                }
                else if(command.Contains("|"))
                {
                    string[] currentCommand = command.Split(" | ");
                    string forceSide = currentCommand[0];
                    string forceUser = currentCommand[1];
                    FirstCommand(forceBook, forceSide, forceUser);
                }
                else
                {
                    string[] currentCommand = command.Split(" -> ");
                    string forceSide = currentCommand[1];
                    string forceUser = currentCommand[0];
                    SecondCommand(forceBook, forceSide, forceUser);
                }
            }
        }

        static void PrintResult(Dictionary<string, List<string>> forceBook)
        {
            foreach(var side in forceBook)
            {
                if(side.Value.Count > 0)
                {
                    Console.WriteLine($"Side: {side.Key}, Members: {side.Value.Count}");
                    side.Value.Sort();

                    foreach(var user in side.Value)
                    {
                        Console.WriteLine($"! {user}");
                    }
                }
            }
        }
        
        static void SecondCommand(Dictionary<string, List<string>> forceBook,
            string forceSide,
            string forceUser)
        {
            foreach (var side in forceBook)
            {
                if (side.Value.Contains(forceUser))
                {
                    side.Value.Remove(forceUser);
                }
            }

            if (IsSideExist(forceBook, forceSide) == true)
            {
                List<string> list = forceBook[forceSide];
                list.Add(forceUser);
            }
            else
            {
                forceBook.Add(forceSide, new List<string> { forceUser });
            }

            Console.WriteLine($"{forceUser} joins the {forceSide} side!");

        }

        static void FirstCommand(Dictionary<string, List<string>> forceBook,
            string forceSide,
            string forceUser)
        {
            if(IsUserExist(forceBook, forceUser) == false)
            {
                if(IsSideExist(forceBook, forceSide) == false)
                {
                    forceBook.Add(forceSide, new List<string> { forceUser });
                }
                else
                {
                    List<string> list = forceBook[forceSide];
                    list.Add(forceUser);
                }
            }
        }

        static bool IsUserExist(Dictionary<string, List<string>> forceBook,
            string forceUser)
        {
            foreach(var side in forceBook)
            {
                if (side.Value.Contains(forceUser))
                {
                    return true;
                }
            }

            return false;
        }

        static bool IsSideExist(Dictionary<string, List<string>> forceBook,
            string forceSide)
        {
            if (forceBook.ContainsKey(forceSide))
            {
                return true;
            }

            return false;
        }
    }
}
