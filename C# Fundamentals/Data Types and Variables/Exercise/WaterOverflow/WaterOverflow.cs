using System;

namespace WaterOverflow
{
    class WaterOverflow
    {
        static void Main(string[] args)
        {
            int numberOfLines = int.Parse(Console.ReadLine());
            int sumOfLiters = 0;

            for(int i = 1; i <= numberOfLines; i++)
            {
                int liters = int.Parse(Console.ReadLine());
                sumOfLiters += liters;
                
                if(sumOfLiters > 255)
                {
                    Console.WriteLine("Insufficient capacity!");
                    sumOfLiters -= liters;
                }
            }
            if (sumOfLiters <= 255)
            {
                Console.WriteLine(sumOfLiters);
            }
        }
    }
}
