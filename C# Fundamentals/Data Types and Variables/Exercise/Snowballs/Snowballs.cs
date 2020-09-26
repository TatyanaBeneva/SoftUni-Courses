using System;
using System.Numerics;

namespace Snowballs
{
    class Snowballs
    {
        static void Main(string[] args)
        {
            sbyte snowballsNumber = sbyte.Parse(Console.ReadLine());
            BigInteger max = 0;
            short snow = 0;
            short time = 0;
            sbyte quality = 0;

            for(sbyte i = 1; i <= snowballsNumber; i++)
            {
                short snowballSnow = short.Parse(Console.ReadLine());
                short snowballTime = short.Parse(Console.ReadLine());
                sbyte snowballQuality = sbyte.Parse(Console.ReadLine());

                BigInteger snowballValue = BigInteger.Pow(snowballSnow / snowballTime, snowballQuality);

                if (snowballValue >= max)
                {
                    max = snowballValue;
                    snow = snowballSnow;
                    time = snowballTime;
                    quality = snowballQuality;
                }
            }

            Console.WriteLine($"{snow} : {time} = {max} ({quality})");
        }
    }
}
