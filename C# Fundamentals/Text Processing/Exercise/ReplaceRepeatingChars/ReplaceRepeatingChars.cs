using System;
using System.Collections.Generic;
using System.Linq;

namespace ReplaceRepeatingChars
{
    class ReplaceRepeatingChars
    {
        static void Main(string[] args)
        {
            char[] text = Console.ReadLine().ToCharArray();
            List<char> removedtext = new List<char>();
            
            foreach(char current in text)
            {
                removedtext.Add(current);
            }

            for(int i = 1; i < removedtext.Count; i++)
            {
                char previous = removedtext[i - 1];
                char current = removedtext[i];

                if(previous == current)
                {
                    removedtext.RemoveAt(i);
                    i--;
                }
            }

            Console.WriteLine(string.Join("", removedtext));
        }
    }
}
