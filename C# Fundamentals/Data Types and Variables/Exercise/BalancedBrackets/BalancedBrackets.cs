using System;

namespace BalancedBrackets
{
    class BalancedBrackets
    {
        static void Main(string[] args)
        {
            int numberOfLines = int.Parse(Console.ReadLine());
            int openingBrecket = 0;
            int closeingBrecket = 0;

            for (int i = 1; i <= numberOfLines; i++)
            {
                string someString = Console.ReadLine();

                switch (someString)
                {
                    case "(":
                        openingBrecket++;
                        break;
                    case ")":
                        closeingBrecket++;
                        if (openingBrecket - closeingBrecket != 0)
                        {
                            Console.WriteLine("UNBALANCED");
                            return;
                        }
                        break;
                }
                              
            }

            if(openingBrecket == closeingBrecket)
            {
                Console.WriteLine("BALANCED");
            }
            else
            {
                Console.WriteLine("UNBALANCED");
            }
        }
    }
}
