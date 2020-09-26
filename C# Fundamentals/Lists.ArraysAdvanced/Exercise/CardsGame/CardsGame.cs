using System;
using System.Collections.Generic;
using System.Linq;

namespace CardsGame
{
    class CardsGame
    {
        static void Main(string[] args)
        {
            List<int> firstPlayer = Console.ReadLine().Split(" ").Select(int.Parse).ToList();
            List<int> secondPlayer = Console.ReadLine().Split(" ").Select(int.Parse).ToList();
            PlayersCards(firstPlayer, secondPlayer);
        }

        static void PlayersCards(List<int> firstPlayer, List<int> secondPlayer)
        {
            while(firstPlayer.Count != 0 && secondPlayer.Count != 0)
            {
                if(firstPlayer[0] == secondPlayer[0])
                {
                    firstPlayer.Remove(firstPlayer[0]);
                    secondPlayer.Remove(secondPlayer[0]);
                }
                else if(firstPlayer[0] > secondPlayer[0])
                {
                    firstPlayer.Add(firstPlayer[0]);
                    firstPlayer.Remove(firstPlayer[0]);
                    firstPlayer.Add(secondPlayer[0]);
                    secondPlayer.Remove(secondPlayer[0]);
                }
                else
                {
                    secondPlayer.Add(secondPlayer[0]);
                    secondPlayer.Remove(secondPlayer[0]);
                    secondPlayer.Add(firstPlayer[0]);
                    firstPlayer.Remove(firstPlayer[0]);
                }
            }
            if(firstPlayer.Count != 0)
            {
                Console.WriteLine($"First player wins! Sum: {firstPlayer.Sum()}");
            }
            else
            {
                Console.WriteLine($"Second player wins! Sum: {secondPlayer.Sum()}");
            }
        }
    }
}
