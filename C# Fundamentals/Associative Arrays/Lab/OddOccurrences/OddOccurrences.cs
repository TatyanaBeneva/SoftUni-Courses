using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace OddOccurrences
{
    class OddOccurrences
    {
        static void Main(string[] args)
        {
            string[] input = Console.ReadLine().Split(" ");
            Dictionary<string, int> count = new Dictionary<string, int>();

            foreach(string word in input)
            {
                string inputInLowerCase = word.ToLower();

                if (count.ContainsKey(inputInLowerCase))
                {
                    count[inputInLowerCase]++;
                }
                else
                {
                    count.Add(inputInLowerCase, 1);
                }
            }
            StringBuilder result = new StringBuilder();

            foreach (var counts in count)
            {
                if(counts.Value % 2 != 0)
                {                   
                    result.Append(counts.Key);
                    result.Append(" ");
                }
            }

            Console.WriteLine(result);
        }
    }
}
