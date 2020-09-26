using System;
using System.Collections.Generic;

namespace Username
{
    class Username
    {
        static void Main(string[] args)
        {
            string userName = Console.ReadLine();

            while (true)
            {
                string command = Console.ReadLine();

                if(command == "Sign up")
                {
                    break;
                }
                else
                {
                    string[] currentCommand = command.Split(" ");

                    switch (currentCommand[0])
                    {
                        case "Case":
                            userName = CaseCommand(userName, currentCommand);
                            Console.WriteLine(userName);
                            break;
                        case "Reverse":
                            ReverseCommand(userName, currentCommand);
                            break;
                        case "Cut":
                            string substring = currentCommand[1];

                            if(userName.Contains(substring) == true)
                            {
                                userName = CutCommand(userName, substring);
                                Console.WriteLine(userName);
                            }
                            else
                            {
                                Console.WriteLine($"The word {userName} doesn't contain {substring}.");
                            }
                            break;
                        case "Replace":
                            char toReplace = char.Parse(currentCommand[1]);
                            userName = userName.Replace(toReplace, '*');
                            Console.WriteLine(userName);
                            break;
                        case "Check":
                            CheckCommand(userName, currentCommand);
                            break;
                    }
                }
            }
        }
        static void CheckCommand(string userName, string[] currentCommand)
        {
            char validChar = char.Parse(currentCommand[1]);

            if (userName.Contains(validChar) == true)
            {
                Console.WriteLine("Valid");
            }
            else
            {
                Console.WriteLine($"Your username must contain {validChar}.");
            }
        }

        static string CutCommand(string userName, string substring)
        {
            int startIndex = userName.IndexOf(substring);
            string text = userName.Remove(startIndex, substring.Length);
            return text;
        }

        static bool IsIndexValidForReverseCommand(string userName, int startIndex, int endIndex)
        {
            if ((startIndex >= 0 && startIndex < userName.Length - 1) && (endIndex <= userName.Length - 1 && endIndex > 0))
            {
                return true;
            }

            return false;
        }

        static void ReverseCommand(string userName, string[] currentCommand)
        {
            int startIndex = int.Parse(currentCommand[1]);
            int endIndex = int.Parse(currentCommand[2]);

            if (IsIndexValidForReverseCommand(userName, startIndex, endIndex) == true)
            {
                string text = "";

                for (int i = endIndex; i >= startIndex; i--)
                {
                    text += userName[i];
                }

                Console.WriteLine(text);
            }            
        }

        static string CaseCommand(string userName, string[] currentCommand)
        {
            string text = "";
            if(currentCommand[1] == "lower")
            {
                text = userName.ToLower();
            }
            else
            {
                text = userName.ToUpper();
            }

            return text;
        }
    }
}
