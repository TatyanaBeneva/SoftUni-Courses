using System;
using System.Linq;

namespace ArrayRotation
{
    class ArrayRotation
    {
        static void Main(string[] args)
        {
            int[] input = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int numberOfRotations = int.Parse(Console.ReadLine());

            for (int j = 0; j < numberOfRotations; j++)
            {
                int currentNumber = input[0];
                    for (int i = 0; i < input.Length -1; i++)
                    {
                    input[i] = input[i + 1];
                    }

                input[input.Length - 1] = currentNumber;
            }
            
            
            Console.WriteLine("{0}", string.Join(" ", input));
        }
    }
}
