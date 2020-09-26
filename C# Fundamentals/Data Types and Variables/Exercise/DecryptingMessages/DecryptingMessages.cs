using System;

namespace DecryptingMessages
{
    class DecryptingMessages
    {
        static void Main(string[] args)
        {
            int key = int.Parse(Console.ReadLine());
            int numberOfLines = int.Parse(Console.ReadLine());
            string messeges = "";
            for (int i = 1; i <= numberOfLines; i++)
            {
                char alfabeth = char.Parse(Console.ReadLine());
                messeges += (char)(key + alfabeth);
            }

            Console.WriteLine(messeges);
        }
    }
}
