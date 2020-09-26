using System;
using System.Text;

namespace EmailValidator
{
    class Program
    {
        static void Main(string[] args)
        {
            string email = Console.ReadLine();

            while (true)
            {
                string currentCommand = Console.ReadLine();

                if(currentCommand == "Complete")
                {
                    break;
                }
                else
                {
                    string[] command = currentCommand.Split(" ");

                    switch (command[0])
                    {
                        case "Make":

                            if(command[1] == "Lower")
                            {
                                email = email.ToLower();
                            }
                            else
                            {
                                email = email.ToUpper();
                            }

                            Console.WriteLine(email);
                            break;
                        case "GetDomain":
                            GetDomainCommand(email, command);
                            break;
                        case "GetUsername":
                            GetUsernameCommand(email);
                            break;
                        case "Replace":
                            char oldChar = char.Parse(command[1]);
                            email = email.Replace(oldChar, '-');
                            Console.WriteLine(email);
                            break;
                        case "Encrypt":
                            EncryptCommand(email);
                            break;
                    }
                }
            }
        }
        static void EncryptCommand(string email)
        {
            int[] charsValue = new int[email.Length];

            for (int i = 0; i < email.Length; i++)
            {
                int current = email[i];
                charsValue[i] = current;
            }

            Console.WriteLine(string.Join(" ", charsValue));
        }

        static void GetUsernameCommand(string email)
        {
            if (email.Contains('@'))
            {
                int index = email.IndexOf('@');
                string username = email.Substring(0, index);
                Console.WriteLine(username);
            }
            else
            {
                Console.WriteLine($"The email {email} doesn't contain the @ symbol.");
            }
        }

        static void GetDomainCommand(string email, string[] command)
        {
            int count = int.Parse(command[1]);
            string domein = email.Substring(email.Length - count, count);
            Console.WriteLine(domein);
        }
    }
}
