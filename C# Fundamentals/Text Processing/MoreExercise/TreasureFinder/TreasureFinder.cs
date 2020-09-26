using System;
using System.Linq;

namespace TreasureFinder
{
    class TreasureFinder
    {
        static void Main(string[] args)
        {
            int[] keys = Console.ReadLine().Split().Select(int.Parse).ToArray();
            string command = Console.ReadLine();
            int index = 0;
            string text = string.Empty;

            while (true)
            {
                if(command == "find")
                {
                    break;
                }
                else
                {
                    for(int j = 0; j < command.Length; j++)
                    {
                        int newChar = command[j] - keys[index];
                        char chars = Convert.ToChar(newChar);
                        text += chars;
                        index++;
                        if (index == keys.Length)
                        {
                            index = 0;
                        }
                    }
                }

                string type = string.Empty;
                
                for(int i = 1; i < text.Length; i++)
                {
                    if(text[i - 1] == '&')
                    {
                        for(int k = i; k < text.Length; k++)
                        {
                            if(text[k] == '&')
                            {
                                break;
                            }
                            else
                            {
                                type += text[k];
                            }
                        }

                        break;
                    }
                }

                int indexOfFirstCordinate = text.IndexOf('<');
                int indexOfLastCordinate = text.IndexOf('>');
                string cordinate = text.Substring(indexOfFirstCordinate + 1, indexOfLastCordinate - indexOfFirstCordinate - 1);

                Console.WriteLine($"Found {type} at {cordinate}");
                text = string.Empty;
                index = 0;

                command = Console.ReadLine();
            }
        }
    }
}
