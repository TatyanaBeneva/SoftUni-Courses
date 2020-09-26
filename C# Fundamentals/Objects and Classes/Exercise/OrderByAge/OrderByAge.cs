using System;
using System.Collections.Generic;
using System.Linq;

namespace OrderByAge
{
    class OrderByAge
    {
        static void Main(string[] args)
        {
            string command = Console.ReadLine();
            var listOfInfo = new List<PersonInfo>();

            while(command != "End")
            {
                string[] currentPerson = command.Split(" ");
                string personName = currentPerson[0];
                string ID = currentPerson[1];
                sbyte age = sbyte.Parse(currentPerson[2]);

                PersonInfo person = new PersonInfo()
                {
                    Name = personName,
                    ID = ID,
                    Age = age
                };

                listOfInfo.Add(person);

                command = Console.ReadLine();
            }

            var orderedByAgeList = new List<PersonInfo>();
            orderedByAgeList = listOfInfo.OrderBy(o => o.Age).ToList();

            foreach(PersonInfo person in orderedByAgeList)
            {
                Console.WriteLine($"{person.Name} with ID: {person.ID} is {person.Age} years old.");
            }
        }
    }
}
