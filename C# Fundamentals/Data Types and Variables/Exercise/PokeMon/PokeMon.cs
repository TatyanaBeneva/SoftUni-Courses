using System;

namespace PokeMon
{
    class PokeMon
    {
        static void Main(string[] args)
        {
            int pokePower = int.Parse(Console.ReadLine());
            int distance = int.Parse(Console.ReadLine());
            sbyte exhaustionFactor = sbyte.Parse(Console.ReadLine());
            int countOfTrgets = 0;
            double originPower = pokePower * 0.50;

            while(pokePower >= distance)
            {
                if(pokePower == originPower)
                {
                    if(exhaustionFactor > 0)
                    {
                        pokePower = pokePower / exhaustionFactor;
                    }

                    if(pokePower < distance)
                    {
                        break;
                    }
                }

                pokePower -= distance;
                countOfTrgets++;
            }

            Console.WriteLine(pokePower);
            Console.WriteLine(countOfTrgets);
        }
    }
}
