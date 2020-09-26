using System;
using System.Collections.Generic;
using System.Linq;

namespace OldestFamilyMember
{
    class OldestFamilyMember
    {
        static void Main(string[] args)
        {
            var currentFamily = new Family();
            int numOfLines = int.Parse(Console.ReadLine());

            for(int i = 0; i < numOfLines; i++)
            {
                string[] input = Console.ReadLine().Split();

                var member = new Person(input[0], int.Parse(input[1]));

                currentFamily.OrderPersons.Add(member);
            }
            Family family = new Family();
            family = currentFamily;
            Person oldestMember = family.GetOldestMember();
            Console.WriteLine("{0} {1}", oldestMember.Name, oldestMember.Age);
        }
    }
}
