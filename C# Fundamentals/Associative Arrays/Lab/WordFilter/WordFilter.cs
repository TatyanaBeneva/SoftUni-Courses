using System;
using System.Linq;

namespace WordFilter
{
    class WordFilter
    {
        static void Main(string[] args)
        {
            string[] words = Console.ReadLine().Split(" ").Where(o => o.Length % 2 == 0).ToArray();
            Console.WriteLine(string.Join(Environment.NewLine, words));
        }
    }
}
