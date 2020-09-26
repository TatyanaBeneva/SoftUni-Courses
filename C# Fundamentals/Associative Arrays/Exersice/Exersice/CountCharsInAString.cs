using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CountCharsInAString
{
    class CountCharsInAString
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            var numberOfChars = new Dictionary<char, int>();

            for(int i = 0; i < text.Length; i++)
            {
                char current = text[i];

                if(current == ' ')
                {
                    continue;
                }
                else
                {
                    if (numberOfChars.ContainsKey(current))
                    {
                        numberOfChars[current]++;
                    }
                    else
                    {
                        numberOfChars.Add(current, 1);
                    }
                }
            }

            foreach (var counts in numberOfChars)
            {
                Console.WriteLine($"{counts.Key} -> {counts.Value}");
            }            
        }
    }
}
