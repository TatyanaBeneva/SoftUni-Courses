using System;

namespace SpiceMustFlow
{
    class SpiceMustFlow
    {
        static void Main(string[] args)
        {
            int fullSpice = int.Parse(Console.ReadLine());
            int spiceAfterTaking = fullSpice;
            int allSpice = 0;
            int daysOfWork = 0;

            if (spiceAfterTaking >= 100)
            {
                allSpice += (spiceAfterTaking - 26);
                daysOfWork++;
            }

            while (spiceAfterTaking >= 100)
            {
                spiceAfterTaking -= 10;

                if(spiceAfterTaking >= 100)
                {
                    allSpice += (spiceAfterTaking - 26);
                    daysOfWork++;
                }
                else
                {
                    allSpice -= 26;
                    break;
                }
            }

            Console.WriteLine(daysOfWork);
            Console.WriteLine(allSpice);
        }
    }
}
