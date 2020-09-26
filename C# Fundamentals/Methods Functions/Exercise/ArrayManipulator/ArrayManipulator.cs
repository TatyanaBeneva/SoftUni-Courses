using System;
using System.Linq;

namespace _11._Array_Manipulator
{
    class Program
    {
        static void Main()
        {
            int[] arr = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();

            string input = Console.ReadLine();

            while (input != "end")
            {
                string[] commands = input.Split(" ");

                if (commands[0] == "exchange")
                {
                    int splitIndex = int.Parse(commands[1]);
                    if (splitIndex < arr.Length && splitIndex >= 0)
                    {
                        Exchange(arr, splitIndex);
                    }
                    else
                    {
                        Console.WriteLine("Invalid index");
                    }
                }

                else if (commands[0] == "max" || commands[0] == "min")
                {
                    Console.WriteLine(EvenOddMaxMin(arr, commands[0], commands[1]));
                }

                else if (commands[0] == "first" || commands[0] == "last")
                {
                    int count = int.Parse(commands[1]);

                    if (count <= arr.Length)
                    {
                        Console.WriteLine("[" + FirstLast(EvenOdd(arr, commands[2]), commands[0], count) + "]");
                    }
                    else
                    {
                        Console.WriteLine("Invalid count");
                    }
                }

                input = Console.ReadLine();
            }

            Console.WriteLine("[" + string.Join(", ", arr) + "]");
        }

        static void Exchange(int[] arr, int splitIndex)
        {
            int[] exchangedArr = new int[arr.Length];
            int indexExchArr = 0;

            for (int i = splitIndex + 1; i < arr.Length; i++)
            {
                exchangedArr[indexExchArr] = arr[i];
                indexExchArr++;
            }

            for (int i = 0; i <= splitIndex; i++)
            {
                exchangedArr[indexExchArr] = arr[i];
                indexExchArr++;
            }

            Array.Copy(exchangedArr, arr, arr.Length);
        }

        static string EvenOddMaxMin(int[] arr, string maxMin, string evenOdd)
        {
            int index = -1;
            int max = int.MinValue;
            int min = int.MaxValue;

            int resultFromModDiv = 0;
            if (evenOdd == "odd")
            {
                resultFromModDiv = 1;
            }

            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] % 2 == resultFromModDiv)
                {
                    if (maxMin == "min")
                    {
                        if (arr[i] <= min)
                        {
                            index = i;
                            min = arr[i];
                        }
                    }
                    else if (maxMin == "max")
                    {
                        if (arr[i] >= max)
                        {
                            index = i;
                            max = arr[i];
                        }
                    }
                }
            }

            if (index >= 0)
            {
                return index.ToString();
            }

            return "No matches";
        }

        static int[] EvenOdd(int[] arr, string evenOdd)
        {
            int[] evenOrOdd = new int[arr.Length];
            int index = 0;

            int resultFromModDiv = 0;
            if (evenOdd == "odd")
            {
                resultFromModDiv = 1;
            }

            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] % 2 == resultFromModDiv)
                {
                    evenOrOdd[index] = arr[i];
                    index++;
                }
            }

            arr = new int[index];
            Array.Copy(evenOrOdd, arr, index);

            return arr;
        }

        static string FirstLast(int[] arr, string firstLast, int count)
        {
            int[] newArr = new int[arr.Length];
            int index = 0;

            if (firstLast == "first")
            {
                for (int i = 0; i < count && i < arr.Length; i++)
                {
                    newArr[index] = arr[i];
                    index++;
                }
            }
            else if (firstLast == "last")
            {
                if (count > arr.Length)
                {
                    count = arr.Length;
                }

                for (int i = arr.Length - count; i < arr.Length; i++)
                {
                    newArr[index] = arr[i];
                    index++;
                }
            }

            arr = new int[index];

            Array.Copy(newArr, arr, index);

            return string.Join(", ", arr);
        }
    }
}

//using System;
//using System.Linq;

//namespace ArrayManipulator
//{
//    class ArrayManipulator
//    {
//        static void Main(string[] args)
//        {
//            int[] inputData = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
//            string command = Console.ReadLine();

//            while(command != "end")
//            {
//                string[] currentCommand = command.Split(" ").ToArray();

//                MaxEven(inputData, currentCommand);
//                MaxOdd(inputData, currentCommand);
//                MinEven(inputData, currentCommand);
//                MinOdd(inputData, currentCommand);
//                FirstCountEven(inputData, currentCommand);
//                FirstCountOdd(inputData, currentCommand);
//                LastCountEven(inputData, currentCommand);
//                LastCountOdd(inputData, currentCommand);               

//                if (currentCommand[0] == "exchange")
//                {
//                    if (int.Parse(currentCommand[1]) > inputData.Length)
//                    {
//                        Console.WriteLine("Invalid index");
//                    }
//                }
//                    command = Console.ReadLine();
//            }
//        }

//        static void ExchangeCommand(int[] inputData, string[] currentCommand)
//        {
//            if (currentCommand[0] == "exchange")
//            {               
//                for (int i = 1; i <= int.Parse(currentCommand[1]); i++)
//                    {

//                    if (int.Parse(currentCommand[1]) > inputData.Length)
//                    {
//                        break;
//                    }
//                    int firtsNum = inputData[0];

//                        for (int j = 0; j < inputData.Length; j++)
//                        {
//                            if (j == inputData.Length - 1)
//                            {
//                                inputData[j] = firtsNum;
//                                break;
//                            }
//                            else
//                            {
//                                inputData[j] = inputData[j + 1];
//                            }
//                        }
//                    }
//                if (int.Parse(currentCommand[1]) <= inputData.Length)
//                {
//                    Console.WriteLine($"[{string.Join(", ", inputData)}]");
//                }


//            }
//        }

//        static void MaxEven(int[] inputData, string[] currentCommand)
//        {
//            if(currentCommand[0] == "max")
//            {
//                if(currentCommand[1] == "even")
//                {
//                    int maxEven = int.MinValue;
//                    int index = 0;
//                    for(int i = 0; i < inputData.Length; i++)
//                    {
//                        if(inputData[i] % 2 == 0 && inputData[i] >= maxEven)
//                        {
//                            maxEven = inputData[i];
//                            index = i;
//                        }
//                    }
//                    if (maxEven != int.MinValue)
//                    {
//                        Console.WriteLine(index);
//                    }
//                    else
//                    {
//                        Console.WriteLine("No matches");
//                    }
//                }
//            }
//        }

//        static void MinEven(int[] inputData, string[] currentCommand)
//        {
//            if (currentCommand[0] == "min")
//            {
//                if (currentCommand[1] == "even")
//                {
//                    int minEven = int.MaxValue;
//                    int index = 0;
//                    for (int i = 0; i < inputData.Length; i++)
//                    {
//                        if (inputData[i] % 2 == 0 && inputData[i] <= minEven)
//                        {
//                            minEven = inputData[i];
//                            index = i;
//                        }
//                    }
//                    if (minEven != int.MaxValue)
//                    {
//                        Console.WriteLine(index);
//                    }
//                    else
//                    {
//                        Console.WriteLine("No matches");
//                    }
//                }
//            }
//        }

//        static void MaxOdd(int[] inputData, string[] currentCommand)
//        {
//            if (currentCommand[0] == "max")
//            {
//                if (currentCommand[1] == "odd")
//                {
//                    int maxOdd = int.MinValue;
//                    int index = 0;
//                    for (int i = 0; i < inputData.Length; i++)
//                    {
//                        if (inputData[i] % 2 != 0 && inputData[i] >= maxOdd)
//                        {
//                            maxOdd = inputData[i];
//                            index = i;
//                        }
//                    }
//                    if (maxOdd != int.MinValue)
//                    {
//                        Console.WriteLine(index);
//                    }
//                    else
//                    {
//                        Console.WriteLine("No matches");
//                    }
//                }
//            }
//        }

//        static void MinOdd(int[] inputData, string[] currentCommand)
//        {
//            if (currentCommand[0] == "min")
//            {
//                if (currentCommand[1] == "odd")
//                {
//                    int minOdd = int.MaxValue;
//                    int index = 0;
//                    for (int i = 0; i < inputData.Length; i++)
//                    {
//                        if (inputData[i] % 2 != 0 && inputData[i] <= minOdd)
//                        {
//                            minOdd = inputData[i];
//                            index = i;
//                        }
//                    }
//                    if(minOdd != int.MaxValue)
//                    {
//                        Console.WriteLine(index);
//                    }
//                    else
//                    {
//                        Console.WriteLine("No matches");
//                    }
//                }
//            }
//        }

//        static void FirstCountEven(int[] inputData, string[] currentCommand)
//        {
//            if(currentCommand[0] == "first")
//            {
//                if(currentCommand[2] == "even")
//                {
//                    int[] firstEvenArray = new int[int.Parse(currentCommand[1])];
//                    int counter = 0;
//                    for(int i = 0; i < inputData.Length; i++)
//                    {
//                        if(int.Parse(currentCommand[1]) > inputData.Length)
//                        {
//                            Console.WriteLine("Invalid count");
//                            break;
//                        }
//                        if(inputData[i] % 2 == 0)
//                        {
//                            counter++;
//                            firstEvenArray[counter - 1] = inputData[i];
//                        }
//                        if(counter == int.Parse(currentCommand[1]))
//                        {
//                            break;
//                        }
//                    }
//                    if(counter == int.Parse(currentCommand[1])){
//                        Console.WriteLine($"[{string.Join(", ", firstEvenArray)}]");
//                    }
//                }
//            }
//        }

//        static void FirstCountOdd(int[] inputData, string[] currentCommand)
//        {
//            if (currentCommand[0] == "first")
//            {
//                if (currentCommand[2] == "odd")
//                {
//                    int[] firstOddArray = new int[int.Parse(currentCommand[1])];
//                    int counter = 0;
//                    for (int i = 0; i < inputData.Length; i++)
//                    {
//                        if (int.Parse(currentCommand[1]) > inputData.Length)
//                        {
//                            Console.WriteLine("Invalid count");
//                            break;
//                        }
//                        if (inputData[i] % 2 != 0)
//                        {
//                            counter++;
//                            firstOddArray[counter - 1] = inputData[i];
//                        }
//                        if (counter == int.Parse(currentCommand[1]))
//                        {
//                            break;
//                        }
//                    }
//                    if (counter == int.Parse(currentCommand[1])){
//                        Console.WriteLine($"[{string.Join(", ", firstOddArray)}]");
//                    }
//                }
//            }
//        }

//        static void LastCountEven(int[] inputData, string[] currentCommand)
//        {
//            if (currentCommand[0] == "last")
//            {
//                if (currentCommand[2] == "even")
//                {
//                    int[] lastEvenArray = new int[int.Parse(currentCommand[1])];
//                    int counter = 0;
//                    for (int i = inputData.Length - 1; i >= 0; i--)
//                    {
//                        if (int.Parse(currentCommand[1]) > inputData.Length)
//                        {
//                            Console.WriteLine("Invalid count");
//                            break;
//                        }
//                        if (inputData[i] % 2 == 0)
//                        {
//                            counter++;
//                            lastEvenArray[counter - 1] = inputData[i];
//                        }
//                        if (counter == int.Parse(currentCommand[1]))
//                        {
//                            break;
//                        }
//                    }
//                    if (counter == int.Parse(currentCommand[1])){
//                        Console.WriteLine($"[{string.Join(", ", lastEvenArray)}]");
//                    }
//                }
//            }
//        }

//        static void LastCountOdd(int[] inputData, string[] currentCommand)
//        {
//            if (currentCommand[0] == "last")
//            {
//                if (currentCommand[2] == "even")
//                {
//                    int[] lastOddArray = new int[int.Parse(currentCommand[1])];
//                    int counter = 0;
//                    for (int i = inputData.Length - 1; i >= 0; i--)
//                    {
//                        if (int.Parse(currentCommand[1]) > inputData.Length)
//                        {
//                            Console.WriteLine("Invalid count");
//                            break;
//                        }
//                        if (inputData[i] % 2 != 0)
//                        {
//                            counter++;
//                            lastOddArray[counter - 1] = inputData[i];
//                        }
//                        if (counter == int.Parse(currentCommand[1]))
//                        {
//                            break;
//                        }
//                    }
//                    if (counter == int.Parse(currentCommand[1])) {
//                        Console.WriteLine($"[{string.Join(", ", lastOddArray)}]");
//                    }
//                }
//            }
//        }
//    }
//}
