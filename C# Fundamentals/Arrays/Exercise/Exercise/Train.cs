using System;

namespace Train
{
    class Train
    {
        static void Main(string[] args)
        {
            int numberOfLines = int.Parse(Console.ReadLine());
            int sum = 0;
            string result = "";

            for(int i = 1; i <= numberOfLines; i++)
            {
                int numberOfPeople = int.Parse(Console.ReadLine());
                sum += numberOfPeople;
                result += numberOfPeople + " ";
            }

            Console.WriteLine(result);
            Console.WriteLine(sum);
        }
    }
}
