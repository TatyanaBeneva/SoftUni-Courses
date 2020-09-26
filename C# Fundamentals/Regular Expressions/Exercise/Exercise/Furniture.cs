using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace Furniture
{
    class Furniture
    {
        static void Main(string[] args)
        {
            string regex = @">>(?<name>[A-Za-z\s]+)<<(?<price>\d+(.\d+)?)!(?<count>\d+)";
            double totalSum = 0.0;
            List<string> products = new List<string>();

            while (true)
            {
                string command = Console.ReadLine();

                if(command == "Purchase")
                {
                    break;
                }
                else
                {
                    Match currentProduct = Regex.Match(command, regex, RegexOptions.IgnoreCase);
                    if(currentProduct.Success)
                    {
                        var product = currentProduct.Groups["name"].Value;
                        double price = double.Parse(currentProduct.Groups["price"].Value);
                        int count = int.Parse(currentProduct.Groups["count"].Value);
                        totalSum += (price * count);
                        products.Add(product);
                    }
                }
            }
            Console.WriteLine("Bought furniture:");
            if(products.Count > 0)
            {
                Console.WriteLine(string.Join(Environment.NewLine, products));
            }
            Console.WriteLine($"Total money spend: {totalSum:f2}");
        }
    }
}
