using System;
using System.Collections.Generic;
using System.Text;

namespace ShoppingSpree
{
    class Product
    {
        public Product(string nameOfProduct, int cost)
        {
            Name = nameOfProduct;
            Cost = cost;
        }

        public string Name { get; set; }

        public int Cost { get; set; }
    }
}
