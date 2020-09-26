using System;

namespace PrimeChecker
{
    class PrimeChecker
    {
        static void Main(string[] args)
        {
            int number = int.Parse(Console.ReadLine());

            for (int i = 2; i <= number; i++)
            {
                bool prime = true;               

                for (int j = 2; j < i; j++)
                {
                    if (i % j == 0)
                    {
                        prime = false;
                        break;
                    }
                }

                string boolPrime = prime.ToString().ToLower();
                Console.WriteLine($"{i} -> {boolPrime}");
            }

        }
    }
}
