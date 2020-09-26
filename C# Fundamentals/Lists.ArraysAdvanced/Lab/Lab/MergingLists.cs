using System;
using System.Collections.Generic;
using System.Linq;

namespace Lab
{
    class MergingLists
    {
        static void Main(string[] args)
        {
            List<int> firstList = Console.ReadLine().Split(' ').Select(int.Parse).ToList();
            List<int> secondList = Console.ReadLine().Split(' ').Select(int.Parse).ToList();
            MergeLists(firstList, secondList);
        }

        static void MergeLists(List<int> firstList, List<int> secondList)
        {
            int firstListCount = firstList.Count;
            int secondListCount = secondList.Count;
            int minListCount = Math.Min(firstListCount, secondList.Count);
            int largerListCount = Math.Max(firstListCount, secondList.Count);

            List<int> mergedList = new List<int>(firstListCount + secondListCount);

            for(int i = 0; i < largerListCount; i++)
            {
                if(i < minListCount)
                {
                    if (i < firstListCount)
                    {
                        mergedList.Add(firstList[i]);
                    }
                    if (i < secondListCount)
                    {
                        mergedList.Add(secondList[i]);
                    }
                }
                else
                {
                    if (firstListCount > secondListCount)
                    {
                        mergedList.Add(firstList[i]);
                    }
                    else
                    {
                        mergedList.Add(secondList[i]);
                    }
                }               
            }
            Console.WriteLine(String.Join(" ", mergedList));
        }
    }
}
