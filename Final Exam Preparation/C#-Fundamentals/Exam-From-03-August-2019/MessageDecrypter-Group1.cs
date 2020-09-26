using System;
using System.Text.RegularExpressions;

namespace MessageDecrypter
{
    class MessageDecrypter
    {
        static void Main(string[] args)
        {
            int numberOfLines = int.Parse(Console.ReadLine());

            for(int i = 0; i < numberOfLines; i++)
            {
                string regex = @"^([\$|%])(?<name>[A-Z]([a-z]{2}?)+)\1:\s(\[(?<first>\d+)\]\|)(\[(?<second>\d+)\]\|)(\[(?<third>\d+)\]\|)$";
                string textInput = Console.ReadLine();
                Match match = Regex.Match(textInput, regex);

                if (match.Success == false)
                {
                    Console.WriteLine("Valid message not found!");
                }
                else
                {
                    string name = match.Groups["name"].Value;
                    int first = int.Parse(match.Groups["first"].Value);
                    int second = int.Parse(match.Groups["second"].Value);
                    int third = int.Parse(match.Groups["third"].Value);

                    Console.WriteLine($"{name}: {Convert.ToChar(first)}{Convert.ToChar(second)}{Convert.ToChar(third)}");
                }
            }
        }
    }
}
