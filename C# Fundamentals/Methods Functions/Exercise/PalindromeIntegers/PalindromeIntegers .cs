using System;

namespace PalindromeIntegers
{
    class PalindromeIntegers
    {
        static void Main(string[] args)
        {
            string number = Console.ReadLine();
            while(number != "END")
            {
                CheckIfNumberIsPalindrome(number);
                number = Console.ReadLine();
            }
        }

        static void CheckIfNumberIsPalindrome(string number)
        {
            int counter = 0;
            for(int i = 0; i < Math.Floor((double)number.Length / 2); i++)
            {
                char currentNum = number[i];
                char lastNum = number[number.Length-(i+1)];
                if(currentNum == lastNum)
                {
                    counter++;
                }
            }

            if(counter == Math.Floor((double)number.Length / 2))
            {
                Console.WriteLine("true");
            }
            else
            {
                Console.WriteLine("false");
            }
        }
    }
}
