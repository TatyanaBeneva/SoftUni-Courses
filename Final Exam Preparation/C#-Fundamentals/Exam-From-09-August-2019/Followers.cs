using System;
using System.Collections.Generic;
using System.Linq;

namespace Followers
{
    class Followers
    {
        static void Main(string[] args)
        {
            Dictionary<string, int[]> information = new Dictionary<string, int[]>();

            while (true)
            {
                string command = Console.ReadLine();

                if(command == "Log out")
                {
                    PrintResult(information);
                    break;
                }
                else
                {
                    string[] currentCommand = command.Split(": ");
                    string userName = currentCommand[1];

                    switch (currentCommand[0])
                    {
                        case "New follower":
                            AddCommand(information, userName);
                            break;
                        case "Like":
                            int likes = int.Parse(currentCommand[2]);
                            LikeCommand(information, userName, likes);
                            break;
                        case "Comment":
                            CommentCommand(information, userName);
                            break;
                        case "Blocked":
                            BlockedCommand(information, userName);
                            break;
                    }
                }
            }
        }

        static void PrintResult(Dictionary<string, int[]> information)
        {
            Console.WriteLine($"{information.Count} followers");

            foreach (var current in information.OrderByDescending(x => x.Value[0]).ThenBy(x => x.Key))
            {
                Console.WriteLine($"{current.Key}: {current.Value[0] + current.Value[1]}");
            }
        }

        static void BlockedCommand(Dictionary<string, int[]> information,
            string userName)
        {
            if(IsUserNameExist(information, userName) == true)
            {
                information.Remove(userName);
            }
            else
            {
                Console.WriteLine($"{userName} doesn't exist.");
            }
        }

        static void CommentCommand(Dictionary<string, int[]> information,
            string userName)
        {
            if(IsUserNameExist(information, userName) == true)
            {
                information[userName][1]++;
            }
            else
            {
                information.Add(userName, new int[2] { 0,1});
            }
        }

        static void LikeCommand(Dictionary<string, int[]> information,
            string userName, int likes)
        {           
            if (IsUserNameExist(information, userName) == true)
            {
                information[userName][0] += likes;
            }
            else
            {
                information.Add(userName, new int[2] { likes, 0});
            }
        }

        static void AddCommand(Dictionary<string, int[]> information,
            string userName)
        {
            if(IsUserNameExist(information, userName) == false)
            {
                information.Add(userName, new int[2]);
            }
        }

        static bool IsUserNameExist(Dictionary<string, int[]> information,
            string userName)
        {
            if (information.ContainsKey(userName))
            {
                return true;
            }

            return false;
        }
    }
}
