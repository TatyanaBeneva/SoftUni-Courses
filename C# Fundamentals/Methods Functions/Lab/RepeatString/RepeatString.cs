using System;

namespace RepeatString
{
    class RepeatString
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            int repeatCount = int.Parse(Console.ReadLine());
            Console.WriteLine(RepeatsString(text, repeatCount));
        }

        static string RepeatsString(string text, int repeatCount)
        {
            string reternVelue = string.Empty;
            for(int i = 0; i < repeatCount; i++)
            {
                reternVelue = reternVelue + text;
            }

            return reternVelue;
        }
    }
}
