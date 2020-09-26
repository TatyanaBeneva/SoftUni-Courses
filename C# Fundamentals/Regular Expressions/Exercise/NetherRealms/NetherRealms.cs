using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace NetherRealms
{
    class NetherRealms
    {
        static void Main(string[] args)
        {
            List<string> deamonsNames = Console.ReadLine().Split(new char[] { ',', ' ' }, StringSplitOptions.RemoveEmptyEntries).ToList();
            deamonsNames.Sort();

            for(int i = 0; i < deamonsNames.Count; i++)
            {
                string name = deamonsNames[i];
                int totalHelth = TotalHelth(name);
                double demage = TotalDemage(name);
                Console.WriteLine($"{name} - {totalHelth} health, {demage:f2} damage");
            }


        }

        static double TotalDemage(string name)
        {
            string regexDemage = @"[+-]?\d+\.?\d*";
            string regexMulti = @"[*\/]";
            double sum = 0;
            MatchCollection demage = Regex.Matches(name, regexDemage);

            if(demage.Count > 0)
            {
                MatchCollection multi = Regex.Matches(name, regexMulti);
                foreach (Match match in demage)
                {
                    double current = double.Parse(match.ToString());
                    sum += (current);
                }
                if (multi.Count > 0)
                {
                    foreach(Match match in multi)
                    {
                        if(char.Parse(match.ToString()) == '*')
                        {
                            sum *= 2;
                        }
                        else
                        {
                            sum /= 2;
                        }
                    }
                }
            }

            return sum;
        }

        static int TotalHelth(string name)
        {
            string regexHelth = @"[^0-9*\+\-\.\/]";
            int sum = 0;
            MatchCollection helth = Regex.Matches(name, regexHelth);
            foreach(Match match in helth)
            {
                char current = char.Parse(match.ToString());
                sum += current;
            }

            return sum;
        }
    }
}
