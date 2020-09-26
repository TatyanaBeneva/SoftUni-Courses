using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;

namespace OldestFamilyMember
{
    class Family
    {
        public Family()
        {
            this.OrderPersons = new List<Person>();
        }

        public List<Person> OrderPersons { get; set; }

        public void AddMember(Person member)
        {
            OrderPersons.Add(member);
        }

        public Person GetOldestMember()

        {
            return this.OrderPersons.OrderByDescending(p => p.Age).First();
        }
    }
}
