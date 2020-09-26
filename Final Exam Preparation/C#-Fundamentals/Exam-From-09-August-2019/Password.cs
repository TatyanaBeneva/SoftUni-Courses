using System;
using System.Text;
using System.Text.RegularExpressions;

namespace Password
{
    class Password
    {
        static void Main(string[] args)
        {
            int numberOfLines = int.Parse(Console.ReadLine());
            string regexPassword = @"^(.+)>(?<numbers>\d{3})\|(?<lowerCase>[a-z]{3})\|(?<upperCase>[A-Z]{3})\|(?<simbols>[^<>]{3})<\1$";

            for(int i  = 0; i < numberOfLines; i++)
            {
                string input = Console.ReadLine();
                Match password = Regex.Match(input, regexPassword);

                if (password.Success)
                {
                    Result(password);
                }
                else
                {
                    Console.WriteLine("Try another password!");
                }
            }
        }

        static void Result(Match password)
        {
            StringBuilder correctPassword = new StringBuilder();
            correctPassword.Append(password.Groups["numbers"].Value);
            correctPassword.Append(password.Groups["lowerCase"].Value);
            correctPassword.Append(password.Groups["upperCase"].Value);
            correctPassword.Append(password.Groups["simbols"].Value);

            Console.WriteLine($"Password: {correctPassword}");
        }
    }
}
