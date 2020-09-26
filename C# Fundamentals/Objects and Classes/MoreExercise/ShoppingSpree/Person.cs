using System;
using System.Collections.Generic;
using System.Text;

namespace ShoppingSpree
{
    class Person
    {
        public Person(string nameOfPerson, int moneyHeHave)
        {
            Name = nameOfPerson;
            Money = moneyHeHave;
            Bag = new List<string>();
        }

        public string Name { get; set; }

        public int Money { get; set; }

        public List<string> Bag { get; set; }
    }
}
