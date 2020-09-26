using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Orders
{
    class Orders
    {
        static void Main(string[] args)
        {
            var productsInformation = new Dictionary<string, List<Products>>();

            while (true)
            {
                string command = Console.ReadLine();

                if(command == "buy")
                {
                    break;
                }
                else
                {
                    string[] data = command.Split(" ");
                    string product = data[0];
                    AddTheProduct(productsInformation, product, data);
                }
            }

            foreach(var product in productsInformation)
            {
                double totalPrice = product.Value[0].Price * product.Value[0].Quantity;              
                Console.WriteLine($"{product.Key} -> {totalPrice:f2}");
            }
        }

        static void AddTheProduct(Dictionary<string, List<Products>> productsInformation, string product, string[] data)
        {
            double price = double.Parse(data[1]);
            int quantity = int.Parse(data[2]);
            Products current = new Products();

            if (productsInformation.ContainsKey(product))
            {
                List<Products> list = productsInformation[product];

                if (current.Price != price)
                {
                    current.Price = price;
                }

                current.Quantity= list[0].Quantity + quantity;
                list.Add(current);
                list.RemoveAt(0);
            }
            else
            {
                current.Price = price;
                current.Quantity = quantity;
                List<Products> list = new List<Products>();
                list.Add(current);
                productsInformation.Add(product, list);
            }
        }
    }
}
