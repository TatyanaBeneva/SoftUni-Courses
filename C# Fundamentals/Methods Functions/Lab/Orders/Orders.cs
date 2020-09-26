using System;

namespace Orders
{
    class Orders
    {
        static void Main(string[] args)
        {
            string product = Console.ReadLine();
            int productCount = int.Parse(Console.ReadLine());

            TotalPrice(product, productCount);


        }

        static void TotalPrice(string product, int count)
        {
            switch (product)
            {
                case "coffee":
                    Console.WriteLine("{0:0.00}", count * 1.50);
                    break;
                case "water":
                    Console.WriteLine("{0:0.00}", count * 1.00);
                    break;
                case "coke":
                    Console.WriteLine("{0:0.00}", count * 1.40);
                    break;
                case "snacks":
                    Console.WriteLine("{0:0.00}", count * 2.00);
                    break;
            }
        }
    }
}
