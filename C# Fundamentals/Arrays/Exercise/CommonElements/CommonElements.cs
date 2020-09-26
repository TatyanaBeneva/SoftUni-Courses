using System;
using System.Linq;

namespace CommonElements
{
    class CommonElements
    {
        static void Main(string[] args)
        {
            string[] firstInput = Console.ReadLine().Split().ToArray();
            string[] secondInput = Console.ReadLine().Split().ToArray();
            string result = "";

            for (int i = 0; i < secondInput.Length; i++)
            {
                string currentInputOfSecondArray = secondInput[i];

                for(int j = 0; j < firstInput.Length; j++)
                {
                    string currentInputOfFirstArray = firstInput[j];

                    if(currentInputOfSecondArray == currentInputOfFirstArray)
                    {
                        result += currentInputOfFirstArray + " ";
                    }
                }
            }

            Console.WriteLine(result);
        }
    }
}
