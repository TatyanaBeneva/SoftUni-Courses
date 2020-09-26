using System;

namespace ExtractFile
{
    class ExtractFile
    {
        static void Main(string[] args)
        {
            string[] path = Console.ReadLine().Split("\\");
            string[] lastPath = path[path.Length - 1].Split(".");

            Console.WriteLine($"File name: {lastPath[0]}");
            Console.WriteLine($"File extension: {lastPath[1]}");
        }
    }
}
