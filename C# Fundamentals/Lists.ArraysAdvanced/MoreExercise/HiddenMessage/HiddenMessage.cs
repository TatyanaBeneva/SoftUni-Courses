using System;
using System.Linq;
using System.Collections.Generic;

namespace HiddenMessage
{
    class HiddenMessage
    {
        static void Main(string[] args)
        {
            string inputData = Console.ReadLine();
            TakeNumbersAndCharsFromInput(inputData);
        }

        static void TakeNumbersAndCharsFromInput(string inputData)
        {
            List<string> numbersOfInput = new List<string>();
            string stringOfInput = string.Empty;

            for(int i = 0; i < inputData.Length; i++)
            {
                if(Char.IsNumber(inputData[i]) == true)
                {
                    numbersOfInput.Add($"{inputData[i]}");
                }
                else
                {
                    stringOfInput += inputData[i];
                }
            }

            List<int> takeList = new List<int>();
            List<int> skipList = new List<int>();

            for (int i = 0; i < numbersOfInput.Count; i++)
            {
                if (i % 2 == 0)
                {
                    takeList.Add(int.Parse(numbersOfInput[i]));
                }
                else
                {
                    skipList.Add(int.Parse(numbersOfInput[i]));
                }
            }

            string result = string.Empty;

            for (int i = 0; i < takeList.Count; i++)
            {
                if (takeList[i] > stringOfInput.Length)
                {
                    takeList[i] = stringOfInput.Length;
                }

                for (int j = 0; j < takeList[i]; j++)
                {
                    result += stringOfInput[0];
                    stringOfInput = stringOfInput.Remove(0, 1);
                }

                if (skipList[i] > stringOfInput.Length)
                {
                    if(stringOfInput.Length > 0)
                    {
                        skipList[i] = stringOfInput.Length;
                        stringOfInput = stringOfInput.Remove(0, (skipList[i] - 1));
                    }
                    else
                    {
                        break;
                    }
                }
                else if(stringOfInput.Length > 0)
                {
                    for (int j = 0; j < skipList[i]; j++)
                    {
                        stringOfInput = stringOfInput.Remove(0, 1);
                    }
                }
            }

            Console.WriteLine(result);
        }
    }
}
