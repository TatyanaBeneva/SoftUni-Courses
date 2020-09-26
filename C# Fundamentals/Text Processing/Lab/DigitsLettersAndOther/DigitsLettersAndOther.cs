using System;
using System.Linq;
using System.Text;

namespace DigitsLettersAndOther
{
    class DigitsLettersAndOther
    {
        static void Main(string[] args)
        {
            char[] text = Console.ReadLine().ToCharArray();
            string digits = string.Empty;
            string simbols = string.Empty;
            string chars = string.Empty;

            foreach (var currentChar in text)
            {
                if (char.IsDigit(currentChar))
                {
                    digits += $"{currentChar}";
                }
                else if (char.IsLetter(currentChar))
                {
                    chars += $"{currentChar}";
                }
                else
                {
                    simbols += $"{currentChar}";
                }
            }

            Console.WriteLine(digits);
            Console.WriteLine(chars);
            Console.WriteLine(simbols);
        }
    }
}
