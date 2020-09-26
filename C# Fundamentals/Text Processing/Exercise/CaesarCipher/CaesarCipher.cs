using System;
using System.Linq;
using System.Text;

namespace CaesarCipher
{
    class CaesarCipher
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine();
            StringBuilder text = new StringBuilder();

            foreach(char current in input)
            {
                text.Append((char)(current + 3));
            }

            Console.WriteLine(text);
        }
    }
}
