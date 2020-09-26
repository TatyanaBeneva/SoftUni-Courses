using System;
using System.Collections.Generic;
using System.Linq;

namespace ListOfProducts
{
    class ListOfProducts
    {
        static void Main(string[] args)
        {
            int numberOfLines = int.Parse(Console.ReadLine());
            List<string> productsNames = new List<string>(numberOfLines);
            
            for(int i = 0; i < numberOfLines; i++)
            {
                productsNames.Add(Console.ReadLine());
            }

            SortProduct(productsNames);
            Console.WriteLine(string.Join("\n", productsNames));
        }

        static void SortProduct(List<string> productsNames)
        {
            productsNames.Sort();

            for(int i = 0; i < productsNames.Count; i++)
            {
                productsNames[i] = $"{i + 1}.{productsNames[i]}";
            }
        }
    }
}
