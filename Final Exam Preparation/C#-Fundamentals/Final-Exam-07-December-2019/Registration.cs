using System;
using System.Text.RegularExpressions;

namespace Registration
{
    class Program
    {
        static void Main(string[] args)
        {
            string regex = @"^(U\$)(?<username>[A-Z]([a-z]+){2}?)\1(P@\$)(?<password>([A-Za-z]+){5}?\d+)\3$";
            int numberOfLines = int.Parse(Console.ReadLine());
            int countOfSuccessfulRegistrations = 0;

            for(int i = 0; i < numberOfLines; i++)
            {
                string currentEmail = Console.ReadLine();
                Match email = Regex.Match(currentEmail, regex);

                if (email.Success)
                {
                    string username = email.Groups["username"].Value;
                    string password = email.Groups["password"].Value;
                    countOfSuccessfulRegistrations++;

                    Console.WriteLine("Registration was successful");
                    Console.WriteLine($"Username: {username}, Password: {password}");
                }
                else
                {
                    Console.WriteLine("Invalid username or password");
                }
            }

            Console.WriteLine($"Successful registrations: {countOfSuccessfulRegistrations}");
        }
    }
}
