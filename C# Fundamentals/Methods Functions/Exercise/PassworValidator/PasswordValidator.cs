using System;

namespace PassworValidator
{
    class PasswordValidator
    {
        static void Main(string[] args)
        {
            string password = Console.ReadLine();
            CheckIfPasswordIsBetween6And10Chars(password);
            CheckIfPasswordHaveOnlyLettersAndDiggits(password);
            CheckIfPasswordHaveAtLeast2Diggits(password);            
            CheckIfPasswordIsValid(password);
            
        }

        static void CheckIfPasswordIsBetween6And10Chars(string password)
        {
            if(password.Length < 6 || password.Length > 10)
            {
                Console.WriteLine("Password must be between 6 and 10 characters");
            }
        }

        static void CheckIfPasswordHaveAtLeast2Diggits(string password)
        {
            int countOfDiggits = 0;

            for(int i = 0; i < password.Length; i++)
            {
                if(password[i] >= 48 && password[i] <= 57)
                {
                    countOfDiggits++;
                }
            }

            if(countOfDiggits < 2)
            {
                Console.WriteLine("Password must have at least 2 digits");
            }
        }
        static void CheckIfPasswordHaveOnlyLettersAndDiggits(string password)
        {
            int countOfLetters = 0;

            for(int i = 0; i < password.Length; i++)
            {
                if((password[i] >= 48 && password[i] <= 57) || (password[i] >= 65 && password[i] <= 122))
                {
                    countOfLetters++;
                }
            }

            if(countOfLetters < password.Length)
            {
                Console.WriteLine("Password must consist only of letters and digits");
            }
        }
        static void CheckIfPasswordIsValid(string password)
        {
            int countOfValidations = 0;

            if (password.Length >= 6 && password.Length <= 10)
            {
                countOfValidations++;
            }
            int countOfLetters = 0;

            for (int i = 0; i < password.Length; i++)
            {
                if ((password[i] >= 48 && password[i] <= 57) || (password[i] >= 65 && password[i] <= 122))
                {
                    countOfLetters++;
                }
            }

            if (countOfLetters == password.Length)
            {
                countOfValidations++;
            }

            int countOfDiggits = 0;

            for (int i = 0; i < password.Length; i++)
            {
                if (password[i] >= 48 && password[i] <= 57)
                {
                    countOfDiggits++;
                }
            }

            if (countOfDiggits >= 2)
            {
                countOfValidations++;
            }

            if(countOfValidations == 3)
            {
                Console.WriteLine("Password is valid");
            }
        }

    }
}
