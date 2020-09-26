using System;

namespace LowerOrUpper
{
    class LowerOrUpper
    {
        static void Main(string[] args)
        {
            string word = Console.ReadLine();
            
            if(word == word.ToUpper())
            {
                Console.WriteLine("upper-case");
            }
            else
            {
                Console.WriteLine("lower-case");
            }
        }
    }
}
