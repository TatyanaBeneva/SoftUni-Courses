using System;

namespace StringManipulator
{
    class StringManipulator
    {
        static void Main(string[] args)
        {
            string textInput = Console.ReadLine();

            while (true)
            {
                string command = Console.ReadLine();

                if(command == "End")
                {
                    break;
                }
                else
                {
                    string[] currentCommand = command.Split(" ");

                    switch (currentCommand[0])
                    {
                        case "Translate":
                            textInput = TranslateCommand(textInput, currentCommand);
                            Console.WriteLine(textInput);
                            break;
                        case "Includes":
                            Console.WriteLine(IncludesCommand(textInput, currentCommand));
                            break;
                        case "Start":
                            Console.WriteLine(StartCommand(textInput, currentCommand));
                            break;
                        case "Lowercase":
                            textInput = textInput.ToLower();
                            Console.WriteLine(textInput);
                            break;
                        case "FindIndex":
                            Console.WriteLine(FindIndexCommand(textInput, currentCommand));
                            break;
                        case "Remove":
                            textInput = RemoveCommand(textInput, currentCommand);
                            Console.WriteLine(textInput);
                            break;
                    }
                }
            }

            
        }

        static string TranslateCommand(string textInput, 
            string[] currentCommand)
        {
            char currentChar = char.Parse(currentCommand[1]);
            char replacemantChar = char.Parse(currentCommand[2]);

            string text = textInput.Replace(currentChar, replacemantChar);
            return text;
        }

        static bool IncludesCommand(string textInput,
            string[] currentCommand)
        {
            string word = currentCommand[1];

            if (textInput.Contains(word))
            {
                return true;
            }

            return false;
        }

        static bool StartCommand(string textInput, 
            string[] currentCommand)
        {
            string word = currentCommand[1];

            if (textInput.StartsWith(word))
            {
                return true;
            }

            return false;
        }

        static int FindIndexCommand(string textInput,
            string[] currentCommand)
        {
            char current = char.Parse(currentCommand[1]);
            int index = textInput.LastIndexOf(current);
            return index;
        }

        static string RemoveCommand(string textInput,
            string[] currentCommand)
        {
            int startIndex = int.Parse(currentCommand[1]);
            int count = int.Parse(currentCommand[2]);

            string text = textInput.Remove(startIndex, count);
            return text;
        }
    }
}
