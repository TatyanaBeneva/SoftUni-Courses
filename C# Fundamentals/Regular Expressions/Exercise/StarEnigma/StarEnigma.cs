using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace StarEnigma
{
    class StarEnigma
    {
        static void Main(string[] args)
        {
            int numOfLines = int.Parse(Console.ReadLine());
            List<string> attackedPlanet = new List<string>();
            List<string> destroyedPlanet = new List<string>();

            for (int i = 0; i < numOfLines; i++)
            {
                string text = ChangeTheInputText();
                Matched(text, attackedPlanet, destroyedPlanet);
            }
            attackedPlanet.Sort();
            destroyedPlanet.Sort();
            Console.WriteLine($"Attacked planets: {attackedPlanet.Count}");
            if(attackedPlanet.Count > 0)
            {
                foreach(var attack in attackedPlanet)
                {
                    Console.WriteLine($"-> {attack}");
                }
            }

            Console.WriteLine($"Destroyed planets: {destroyedPlanet.Count}");
            if(destroyedPlanet.Count > 0)
            {
                foreach(var dest in destroyedPlanet)
                {
                    Console.WriteLine($"-> {dest}");
                }
            }
        }

        static void Matched(string text, List<string> attackedPlanet, List<string> destroyedPlanet)
        {
            string regex = @"[^@\-!:>]*@(?<planetName>[A-Z][a-z]+)[^@\-!:>]*\:(?<population>\d*)\!(?<attakType>[DA])\![^@\-!:>]*->(?<soldierCount>\d*)[^@\-!:>]*";
            Match info = Regex.Match(text, regex);
            if(info.Success == true)
            {
                string planetName = info.Groups["planetName"].Value;
                char attakType = char.Parse(info.Groups["attakType"].Value);

                if (attakType == 'A')
                {
                    attackedPlanet.Add(planetName);
                }
                else
                {
                    destroyedPlanet.Add(planetName);
                }
            }            
        }

        static string ChangeTheInputText()
        {
            string text = Console.ReadLine();
            string regexForCount = @"[S,s,T,t,A,a,R,r]";
            int countStar = Regex.Matches(text, regexForCount).Count;
            string goodText = "";

            for(int i = 0; i < text.Length; i++)
            {
                int numOfChar = text[i] - countStar;
                char current = Convert.ToChar(numOfChar);
                goodText += current;
            }

            return goodText;
        }
    }
}
