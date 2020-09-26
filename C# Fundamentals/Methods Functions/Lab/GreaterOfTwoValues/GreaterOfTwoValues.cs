using System;

namespace GreaterOfTwoValues
{
    class GreaterOfTwoValues
    {
        static void Main(string[] args)
        {
            string typeOfValues = Console.ReadLine();
            if(typeOfValues == "int")
            {
                int firtsValue = int.Parse(Console.ReadLine());
                int secondValue = int.Parse(Console.ReadLine());
                Console.WriteLine(ReternGreaterValue(firtsValue, secondValue));
            }
            else if(typeOfValues == "char")
            {
                char firtsValue = char.Parse(Console.ReadLine());
                char secondValue = char.Parse(Console.ReadLine());
                Console.WriteLine(ReternGreaterValue(firtsValue, secondValue));
            }
            else if(typeOfValues == "string")
            {
                string firstValue = Console.ReadLine();
                string secondValue = Console.ReadLine();
                Console.WriteLine(ReternGreaterValue(firstValue, secondValue));
            }
        }

        static int ReternGreaterValue(int firstValue, int secondValue)
        {
            if (firstValue > secondValue)
            {
                return firstValue;
            }

            return secondValue;
        }

        static char ReternGreaterValue(char firstValue, char secondValue)
        {
            if (firstValue > secondValue)
            {
                return firstValue;
            }

            return secondValue;
        }

        static string ReternGreaterValue(string firstValue, string secondValue)
        {
            if (firstValue.CompareTo(secondValue) > 0)
            {
                return firstValue;
            }

            return secondValue;
        }
    }
}
