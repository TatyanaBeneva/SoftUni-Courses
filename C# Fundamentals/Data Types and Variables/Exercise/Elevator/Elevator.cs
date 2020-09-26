
using System;

namespace Elevator
{
    class Elevator
    {
        static void Main(string[] args)
        {
            int numberOfPerson = int.Parse(Console.ReadLine());
            int capacityOfPerson = int.Parse(Console.ReadLine());

            int numberOfFullCourses = (int)Math.Floor((double) numberOfPerson / capacityOfPerson);
            int notFullCourses = numberOfPerson % capacityOfPerson;
            int allCourses = 0;
            
            if(notFullCourses > 0)
            {
                allCourses = numberOfFullCourses + 1;
            }
            else
            {
                allCourses = numberOfFullCourses;
            }

            Console.WriteLine(allCourses);
        }
    }
}
