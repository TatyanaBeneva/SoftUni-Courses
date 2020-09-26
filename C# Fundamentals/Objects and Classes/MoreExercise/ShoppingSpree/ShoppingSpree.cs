using System;
using System.Collections.Generic;
using System.Linq;

namespace ShoppingSpree
{
    class ShoppingSpree
    {
        static void Main(string[] args)
        {
            string[] allPeople = Console.ReadLine().Split(";");
            List<Person> listOfPeoples = new List<Person>();
            AddPersons(allPeople, listOfPeoples);

            string[] allProducts = Console.ReadLine().Split(";");
            List<Product> listOfProducts = new List<Product>();
            AddProducts(allProducts, listOfProducts);

            string command = Console.ReadLine();
            PrintIfPersonBuyProductOrNot(command, listOfPeoples, listOfProducts);

            foreach(Person person in listOfPeoples)
            {
                if(person.Bag.Count > 0)
                {
                    Console.WriteLine($"{person.Name} - {string.Join(", ", person.Bag)}");
                }
                else
                {
                    Console.WriteLine($"{person.Name} - Nothing bought");
                }
            }
            
        }

        static void AddPersons(string[] allPeople, List<Person> listOfPeoples)
        {
            for (int i = 0; i < allPeople.Length; i++)
            {
                string[] currentPeople = allPeople[i].Split("=");
                string nameOfPerson = currentPeople[0];
                int moneyHeHave = int.Parse(currentPeople[1]);
                Person person = new Person(nameOfPerson, moneyHeHave);
                listOfPeoples.Add(person);
            }
        }

        static void AddProducts(string[] allProducts, List<Product> listOfProducts)
        {
            for (int i = 0; i < allProducts.Length; i++)
            {
                string[] currentProduct = allProducts[i].Split("=");
                string nameOfProduct = currentProduct[0];
                int cost = int.Parse(currentProduct[1]);
                Product product = new Product(nameOfProduct, cost);
                listOfProducts.Add(product);
            }
        }

        static void PrintIfPersonBuyProductOrNot(string command, List<Person> listOfPeoples, List<Product> listOfProducts)
        {
            while (command != "END")
            {
                string[] everyPersonBuy = command.Split(" ");
                string nameOfPerson = everyPersonBuy[0];
                string nameOfProduct = everyPersonBuy[1];
                foreach (Person person in listOfPeoples)
                {
                    if (person.Name == nameOfPerson)
                    {
                        foreach (Product product in listOfProducts)
                        {
                            if (product.Name == nameOfProduct)
                            {
                                if (person.Money >= product.Cost)
                                {
                                    person.Bag.Add(nameOfProduct);
                                    person.Money -= product.Cost;
                                    Console.WriteLine($"{person.Name} bought {product.Name}");
                                    break;
                                }
                                else
                                {
                                    Console.WriteLine($"{person.Name} can't afford {product.Name}");
                                    break;
                                }
                            }
                        }
                    }
                }

                command = Console.ReadLine();
            }
        }
    }
}
