using System;

namespace ValidUsernames
{
    class ValidUsernames
    {
        static void Main(string[] args)
        {
            string[] userNames = Console.ReadLine().Split(", ");

            foreach(var currentUser in userNames)
            {
                int count = 0;

                if(currentUser.Length > 3 && currentUser.Length < 16)
                {
                    foreach (char current in currentUser)
                    {
                        if (IsCurrentUserValid(userNames, current) == false)
                        {
                            break;
                        }
                        else
                        {
                            count++;
                        }
                    }
                }

                if(count == currentUser.Length)
                {
                    Console.WriteLine(currentUser);
                }
            }

        }

        static bool IsCurrentUserValid(string[] userNames, char current)
        {
            if (char.IsDigit(current))
            {
                return true;
            }
            else if (char.IsLetter(current))
            {
                return true;
            }
            else if (current == '-')
            {
                return true;
            }
            else if (current == '_')
            {
                return true;
            }

            return false;            
        }
    }
}
