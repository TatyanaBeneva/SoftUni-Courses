using System;
using System.Collections.Generic;
using System.Linq;

namespace AppendArrays
{
    class AppendArrays
    {
        static void Main(string[] args)
        {
            string[] theBigArray = Console.ReadLine().Split("|").ToArray();
            List<int> result = new List<int>(theBigArray.Length);
            for(int i = 1; i <= theBigArray.Length; i++)
            {
                List<int> array = theBigArray[theBigArray.Length - i].Split(" ",StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).ToList();

                for(int j = 0; j < array.Count; j++)
                {
                    result.Add(array[j]);
                }
            }
            Console.WriteLine(string.Join(" ", result));
        }
    }
}
