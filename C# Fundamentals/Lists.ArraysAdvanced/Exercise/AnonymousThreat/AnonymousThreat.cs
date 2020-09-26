using System;
using System.Linq;
using System.Collections.Generic;

namespace AnonymousThreat
{
    class AnonymousThreat
    {
        static void Main(string[] args)
        {
            List<string> input = Console.ReadLine().Split().ToList();

            while (true)
            {
                string[] comand = Console.ReadLine().Split().ToArray();

                if (comand[0] == "3:1")
                {
                    Console.Write(string.Join(" ", input));
                    break;
                }

                else if (comand[0] == "merge")
                {
                    int startIndex = int.Parse(comand[1]);
                    int endIndex = int.Parse(comand[2]);
                    Merge(input, startIndex, endIndex);
                }
                else if (comand[0] == "divide")
                {
                    int index = int.Parse(comand[1]);
                    int partitions = int.Parse(comand[2]);
                    Divide(input, index, partitions);
                }

            }

        }

        static void Merge(List<string> input, int startIndex, int endIndex)
        {
            if (startIndex < 0)
            {
                startIndex = 0;
            }
            if (endIndex > input.Count - 1)
            {
                endIndex = input.Count - 1;
            }

            for (int j = startIndex + 1; j <= endIndex; j++)
            {
                input[startIndex] += input[startIndex + 1];
                input.RemoveAt(startIndex + 1);
            }
        }

        static void Divide(List<string> input, int index, int partitions)
        {
            string partitionData = input[index];
            input.RemoveAt(index);
            int partSize = partitionData.Length / partitions;
            int reminder = partitionData.Length % partitions;

            List<string> tmpData = new List<string>();

            for (int i = 0; i < partitions; i++)
            {
                string tmpString = null;

                for (int p = 0; p < partSize; p++)
                {
                    tmpString += partitionData[(i * partSize) + p];
                }

                if (i == partitions - 1 && reminder != 0)
                {
                    tmpString += partitionData.Substring(partitionData.Length - reminder);
                }

                tmpData.Add(tmpString);
            }

            input.InsertRange(index, tmpData);


        }
    }
}

//using System;
//using System.Collections.Generic;
//using System.Linq;

//namespace AnonymousThreat
//{
//    class AnonymousThreat
//    {
//        static void Main(string[] args)
//        {
//            List<string> input = Console.ReadLine().Split(" ").ToList();
//            string endCommand = Console.ReadLine();

//            while(endCommand != "3:1")
//            {
//                List<string> commands = endCommand.Split(" ").ToList();

//                switch (commands[0])
//                {
//                    case "merge":
//                        MergeIndex(input, commands);
//                        break;
//                    case "divide":
//                        DivideIndex(input, commands);
//                        break;
//                }

//                endCommand = Console.ReadLine();
//            }

//            Console.WriteLine(string.Join(" ", input));
//        }

//        static void MergeIndex(List<string> input, List<string> commands)
//        {
//            int startIndex = int.Parse(commands[1]);
//            int endIndex = int.Parse(commands[2]);
//            string mergeResult = string.Empty;

//            if(endIndex < input.Count && startIndex < input.Count)
//            {
//                for(int i = startIndex; i <= endIndex; i++)
//                {
//                    mergeResult += input[startIndex];
//                    input.RemoveAt(startIndex);
//                }

//                input.Insert(startIndex, mergeResult);
//            }
//            else if(endIndex >= input.Count && startIndex < input.Count && startIndex != input.Count - 1)
//            {
//                endIndex = input.Count - 1;
//                for (int i = startIndex; i <= endIndex; i++)
//                {
//                    mergeResult += input[startIndex];
//                    input.RemoveAt(startIndex);
//                }

//                input.Insert(startIndex, mergeResult);
//            }
//            else
//            {
//                return;
//            }
//        }

//        static void DivideIndex(List<string> input, List<string> commands)
//        {
//            int index = int.Parse(commands[1]);
//            int countOfDividing = int.Parse(commands[2]);

//            if(input[index].Length % countOfDividing == 0)
//            {
//                int numOfChars = input[index].Length / countOfDividing;
//                string result = string.Empty;
//                int i = 0;
//                int nextIndex = 0;
//                for (int e = index; e < (index + countOfDividing); e++)
//                {
//                    for (int j = 0 + i; j < numOfChars + i; j++)
//                    {
//                        result += input[index + nextIndex][j];
//                    }

//                    input.Insert(e, result);
//                    i += numOfChars;
//                    nextIndex++;
//                    result = string.Empty;
//                }

//                input.RemoveAt(index + countOfDividing);
//            }
//            else
//            {
//                int numOfChars = input[index].Length / countOfDividing;
//                string result = string.Empty;
//                int i = 0;
//                int nextIndex = 0;
//                for (int e = index; e < (index + countOfDividing - 1); e++)
//                {
//                    for (int j = 0 + i; j < numOfChars + i; j++)
//                    {
//                        result += input[index + nextIndex][j];
//                    }

//                    input.Insert(e, result);
//                    i += numOfChars;
//                    nextIndex++;
//                    result = string.Empty;
//                }
//                for(int p = (numOfChars * countOfDividing) - (input[index].Length % countOfDividing); p < numOfChars * countOfDividing; p++)
//                {
//                    result += input[index + nextIndex][p];
//                }

//                input.RemoveAt(index + countOfDividing);
//            }
//        }
//    }
//}
