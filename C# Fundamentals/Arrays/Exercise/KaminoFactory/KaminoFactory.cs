using System;
using System.Linq;
namespace KaminoFactory
{
    class KaminoFactory
    {
        static void Main(string[] args)
        {
            int size = int.Parse(Console.ReadLine());
            string input = null;
            int bestCount = 0;
            int bestSum = 0;
            int bestBeginIndex = 0;
            string bestSequense = "";
            int counter = 0;
            int bestCounter = 0;

            while((input = Console.ReadLine()) != "Clone them!")
            {
                string sequense = input.Replace("!", "");
                string[] dnaParts = sequense.Split("0", StringSplitOptions.RemoveEmptyEntries);
                int count = 0;
                int sum = 0;
                string bestSubsequense = "";
                counter++;

                foreach (string dnaPart in dnaParts)
                {
                    if (dnaPart.Length > count)
                    {
                        count = dnaPart.Length;
                        bestSubsequense = dnaPart;

                    }
                    sum += dnaPart.Length;
                }

                int beginIndex = sequense.IndexOf(bestSubsequense);

                if(count > bestCount || (count == bestCount && beginIndex < bestBeginIndex) || (count == bestCount && beginIndex == bestBeginIndex && sum > bestSum) || counter == 1)
                {
                    bestCount = count;
                    bestSequense = sequense;
                    bestBeginIndex = beginIndex;
                    bestSum = sum;
                    bestCounter = counter;
                }
            }

            char[] result = bestSequense.ToCharArray();
            Console.WriteLine($"Best DNA sample {bestCounter} with sum: {bestSum}.");
            Console.WriteLine(string.Join(" ", result));
        }
        //static int indexStartOfTheLongestSubsequence(int[] dna)
        //{
        // This is the 100/100 result

        //    int leftMost = int.MinValue;
        //    int subsequenceMaxInTheArray = 0;
        //    for (int i = 0; i < dna.Length; i++)
        //    {
        //        if (dna[i] == 1)
        //        {
        //            int subsequence = 1;
        //            for (int j = i + 1; j < dna.Length; j++)
        //            {
        //                if (dna[i] == dna[j])
        //                    subsequence++;
        //                else
        //                    break;
        //            }
        //            if (subsequence > subsequenceMaxInTheArray)
        //            {
        //                subsequenceMaxInTheArray = subsequence;
        //                leftMost = i;

        //            }

        //        }
        //    }
        //    return leftMost;

        //}
        //static int Subsequence(int[] dna)
        //{
        //    int subsequenceMaxInTheArray = 0;
        //    for (int i = 0; i < dna.Length; i++)
        //    {
        //        if (dna[i] == 1)
        //        {
        //            int subsequence = 1;
        //            for (int j = i + 1; j < dna.Length; j++)
        //            {
        //                if (dna[i] == dna[j])
        //                    subsequence++;
        //                else
        //                    break;
        //            }
        //            if (subsequence > subsequenceMaxInTheArray)
        //            {
        //                subsequenceMaxInTheArray = subsequence;


        //            }

        //        }
        //    }
        //    return subsequenceMaxInTheArray;
        //}

        //static int MostOnes(int[] dna)
        //{
        //    int mostOnes = 0;
        //    for (int i = 0; i < dna.Length; i++)
        //    {
        //        if (dna[i] == 1)
        //        {
        //            mostOnes++;
        //        }
        //    }
        //    return mostOnes;
        //}

        //static int[] Dna(string entry)
        //{
        //    return entry.Split(new[] { '!' }, StringSplitOptions.RemoveEmptyEntries)
        //            .Select(int.Parse)
        //            .ToArray();

        //}
        //static void Main()
        //{
        //    int dnaLength = int.Parse(Console.ReadLine());
        //    string entry = Console.ReadLine();

        //    int mostLeft = indexStartOfTheLongestSubsequence(Dna(entry));
        //    int longestSubsequenceOnes = Subsequence(Dna(entry));
        //    int mostOnes = int.MinValue;
        //    int sample = 0;
        //    int bestSample = 0;

        //    int[] bestDna = new int[dnaLength];

        //    while (entry != "Clone them!")
        //    {
        //        int[] dna = Dna(entry);
        //        sample++;
        //        int ones = MostOnes(dna);
        //        if (longestSubsequenceOnes < Subsequence(dna))
        //        {
        //            longestSubsequenceOnes = Subsequence(dna);
        //            bestDna = dna;
        //            bestSample = sample;
        //            mostOnes = ones;
        //        }
        //        else if (longestSubsequenceOnes == Subsequence(dna))
        //        {
        //            int leftMostTry = indexStartOfTheLongestSubsequence(dna);
        //            if (mostLeft > leftMostTry)
        //            {
        //                mostLeft = leftMostTry;
        //                bestDna = dna;
        //                bestSample = sample;
        //                mostOnes = ones;

        //            }
        //            else if (mostLeft == leftMostTry)
        //            {

        //                if (mostOnes < ones)
        //                {
        //                    mostOnes = ones;
        //                    bestDna = dna;
        //                    bestSample = sample;
        //                }
        //            }
        //        }


        //        //Console.WriteLine(string.Join(' ', dna));
        //        //Console.WriteLine(Subsequence(dna));
        //        entry = Console.ReadLine();

        //    }
        //    Console.WriteLine($"Best DNA sample {bestSample} with sum: {mostOnes}.");
        //    Console.WriteLine(string.Join(' ', bestDna));

        //int sequenceLength = int.Parse(Console.ReadLine());
        //string input = Console.ReadLine();

        //int[] DNA = new int[sequenceLength];
        //int DNASum = 0;
        //int DNACount = -1;
        //int DNAStartIndex = -1;
        //int DNASample = 0;

        //int sample = 0;
        //while (input != "Clone them!")
        //{
        //    //----------------------------- CURRENT DNA INFO -----------------------------
        //    sample++;
        //    int[] currDNA = input.Split("!", StringSplitOptions.RemoveEmptyEntries)
        //                        .Select(int.Parse)
        //                        .ToArray();
        //    int currCount = 0;
        //    int currStartIndex = 0;
        //    int currEndIndex = 0;
        //    int currDNASum = 0;
        //    bool isCurrDNABetter = false;

        //    int count = 0;
        //    for (int i = 0; i < currDNA.Length; i++)
        //    {
        //        if (currDNA[i] != 1)
        //        {
        //            count = 0;
        //            continue;
        //        }

        //        count++;
        //        if (count > currCount)
        //        {
        //            currCount = count;
        //            currEndIndex = i;
        //        }
        //    }

        //    currStartIndex = currEndIndex - currCount + 1;
        //    currDNASum = currDNA.Sum();

        //    //-------------------- CHECK CURRENT DNA WITH BEST DNA -----------------------
        //    if (currCount > DNACount)
        //    {
        //        isCurrDNABetter = true;
        //    }
        //    else if (currCount == DNACount)
        //    {
        //        if (currStartIndex < DNAStartIndex)
        //        {
        //            isCurrDNABetter = true;
        //        }
        //        else if (currStartIndex == DNAStartIndex)
        //        {
        //            if (currDNASum > DNASum)
        //            {
        //                isCurrDNABetter = true;
        //            }
        //        }
        //    }

        //    if (isCurrDNABetter)
        //    {
        //        DNA = currDNA;
        //        DNACount = currCount;
        //        DNAStartIndex = currStartIndex;
        //        DNASum = currDNASum;
        //        DNASample = sample;
        //    }

        //    //----------------------------------------------------------------------------
        //    input = Console.ReadLine();
        //}

        //Console.WriteLine($"Best DNA sample {DNASample} with sum: {DNASum}.");
        //Console.WriteLine(String.Join(" ", DNA));

        //int arrayLenght = int.Parse(Console.ReadLine());
        //string input = Console.ReadLine();
        //int[] DNA = new int[arrayLenght];
        //int lenght = 0;
        //int index = 0;
        //int sum = 0;
        //int currentRow = 0;
        //int row = 0;

        //while (input != "Clone them!")
        //{
        //    int[] currentDNA = input.Split('!').Select(int.Parse).ToArray();
        //    currentRow++;

        //    int currentSum = 0;
        //    for (int i = 0; i < currentDNA.Length; i++)
        //    {
        //        if (currentDNA[i] == 1)
        //        {
        //            currentSum++;
        //        }
        //    }

        //    int currentLenght = 0;
        //    int currentIndex = 0;

        //    for (int i = 0; i < currentDNA.Length; i++)
        //    {
        //        if (currentDNA[i] == 1)
        //        {

        //            currentLenght++;
        //            if (currentLenght == 1)
        //            {
        //                currentIndex = i;
        //            }

        //            if (currentLenght > lenght || currentLenght == lenght && (currentIndex < index || currentSum > sum))
        //            {
        //                lenght = currentLenght;
        //                index = currentIndex;
        //                row = currentRow;
        //                DNA = currentDNA;
        //                sum = currentSum;

        //            }

        //        }
        //        else
        //        {
        //            currentIndex = 0;
        //            currentLenght = 0;
        //        }

        //    }

        //    input = Console.ReadLine();
        //}

        //if (row == 0)
        //{
        //    row = 1;
        //}

        //Console.WriteLine($"Best DNA sample {row} with sum: {sum}.");
        //Console.WriteLine(string.Join(" ", DNA));
        //}
    }
}
