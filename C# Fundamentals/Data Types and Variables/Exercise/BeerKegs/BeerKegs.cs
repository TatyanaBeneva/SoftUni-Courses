using System;

namespace BeerKegs
{
    class BeerKegs
    {
        static void Main(string[] args)
        {
            int numberOfKegs = int.Parse(Console.ReadLine());
            double max = int.MinValue;
            string model = "";

            for(int i = 1; i <= numberOfKegs; i++)
            {
                string modelOfKeg = Console.ReadLine();
                float radios = float.Parse(Console.ReadLine());
                int height = int.Parse(Console.ReadLine());

                double volume = Math.PI * radios * radios * height;
                if(volume > max)
                {
                    max = volume;
                    model = modelOfKeg;
                }
            }

            Console.WriteLine(model);
        }
    }
}
