using System;
using System.Linq;

namespace EncryptSortAndPrintArray
{
    class EncryptSortAndPrintArray
    {
        static void Main(string[] args)
        {
            int numberOfStrings = int.Parse(Console.ReadLine());
            int[] result = new int[numberOfStrings];

            for(int j = 0; j < numberOfStrings; j++)
            {
                string inputName = Console.ReadLine();
                int sum = 0;

                for (int i = 0; i < inputName.Length; i++)
                {
                    char chars =(char)inputName[i];
                    int number = (char)chars;

                    switch (chars)
                    {
                        case 'a':
                            sum += (number * inputName.Length);
                            break;
                        case 'e':
                            sum += (number * inputName.Length);
                            break;
                        case 'i':
                            sum += (number * inputName.Length);
                            break;
                        case 'o':
                            sum += (number * inputName.Length);
                            break;
                        case 'u':
                            sum += (number * inputName.Length);
                            break;
                        default:
                            sum += (int)Math.Floor((double)number / inputName.Length);
                            break;
                    }
                }

                result[j] = sum;
            }
            Array.Sort(result);
            for (int i = 0; i < result.Length; i++)
            {
                Console.WriteLine(result[i]);
            }
        }
    }
}
