using System;

namespace LettersChangeNumbers
{
    class LettersChangeNumbers
    {
        static void Main(string[] args)
        {
            string[] input = Console.ReadLine().Split(new[] { ' ', '\t' }, StringSplitOptions.RemoveEmptyEntries);
            int position = 0;
            decimal currentResult = 0;
            decimal sum = 0;

            foreach(string currentInput in input)
            {
                int number = int.Parse(currentInput.Remove(currentInput.Length - 1, 1).Remove(0, 1));
                char firstLetter = currentInput[0];
                position = Positions(firstLetter);
                if (char.IsLower(firstLetter))
                {
                    currentResult = number * position;
                }
                else
                {
                    currentResult = (decimal)number / position;
                }

                char lastLetter = currentInput[currentInput.Length - 1];
                position = Positions(lastLetter);
                if (char.IsLower(lastLetter))
                {
                    currentResult += position;
                    sum += currentResult;
                }
                else
                {
                    currentResult -= position;
                    sum += currentResult;
                }
            }

            Console.WriteLine($"{sum:f2}");
        }

        static int Positions(char letter)
        {
            int position = 0;
            switch (letter)
            {
                case 'a':
                case 'A': position = 1; break;
                case 'b':
                case 'B': position = 2; break;
                case 'c':
                case 'C': position = 3; break;
                case 'd':
                case 'D': position = 4; break;
                case 'e':
                case 'E': position = 5; break;
                case 'f':
                case 'F': position = 6; break;
                case 'g':
                case 'G': position = 7; break;
                case 'h':
                case 'H': position = 8; break;
                case 'i':
                case 'I': position = 9; break;
                case 'j':
                case 'J': position = 10; break;
                case 'k':
                case 'K': position = 11; break;
                case 'l':
                case 'L': position = 12; break;
                case 'm':
                case 'M': position = 13; break;
                case 'n':
                case 'N': position = 14; break;
                case 'o':
                case 'O': position = 15; break;
                case 'p':
                case 'P': position = 16; break;
                case 'q':
                case 'Q': position = 17; break;
                case 'r':
                case 'R': position = 18; break;
                case 's':
                case 'S': position = 19; break;
                case 't':
                case 'T': position = 20; break;
                case 'u':
                case 'U': position = 21; break;
                case 'v':
                case 'V': position = 22; break;
                case 'W':
                case 'w': position = 23; break;
                case 'x':
                case 'X': position = 24; break;
                case 'y':
                case 'Y': position = 25; break;
                case 'z':
                case 'Z': position = 26; break;
            }

            return position;
        }
    }
}
