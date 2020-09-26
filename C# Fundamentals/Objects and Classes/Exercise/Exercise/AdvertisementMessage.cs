using System;
using System.Collections.Generic;

namespace AdvertisementMessage
{
    class AdvertisementMessage
    {
        static void Main(string[] args)
        {
            int numOfLines = int.Parse(Console.ReadLine());
            List<string> phrases = new List<string>(){
                "Excellent product.",
                "Such a great product.",
                "I always use that product.",
                "Best product of its category.",
                "Exceptional product.",
                "I can’t live without this product."
            };
            List<string> events = new List<string>()
            {
                "Now I feel good.",
                "I have succeeded with this product.",
                "Makes miracles. I am happy of the results!",
                "I cannot believe but now I feel awesome.",
                "Try it yourself, I am very satisfied.",
                "I feel great!"
            };
            List<string> authors = new List<string>() {
                "Diana",
                "Petya",
                "Stella",
                "Elena",
                "Katya",
                "Iva",
                "Annie",
                "Eva"
            };
            List<string> cities = new List<string>() {
                "Burgas",
                "Sofia",
                "Plovdiv",
                "Varna",
                "Ruse"
            };

            for (int i = 0; i < numOfLines; i++)
            {
                Shiffle(phrases, events, authors, cities);
                Console.WriteLine($"{phrases[0]} {events[0]} {authors[0]} – {cities[0]}.");
            }
        }

        static void Shiffle(List<string> phrases,
            List<string> events,
            List<string> authors,
            List<string> cities)
        {
            Random rnd = new Random();
            int countPhrases = phrases.Count;
            int countEvents = events.Count;
            int countAuthors = authors.Count;
            int countCities = cities.Count;

            while (countPhrases > 1)
            {
                countPhrases--;
                int randomPosition = rnd.Next(countPhrases + 1);
                string valueOfRandomElement = phrases[randomPosition];
                phrases[randomPosition] = phrases[countPhrases];
                phrases[countPhrases] = valueOfRandomElement;
            }
            while (countEvents > 1)
            {
                countEvents--;
                int randomPosition = rnd.Next(countEvents + 1);
                string valueOfRandomElement = events[randomPosition];
                events[randomPosition] = events[countEvents];
                events[countEvents] = valueOfRandomElement;
            }
            while (countAuthors > 1)
            {
                countAuthors--;
                int randomPosition = rnd.Next(countAuthors + 1);
                string valueOfRandomElement = authors[randomPosition];
                authors[randomPosition] = authors[countAuthors];
                authors[countAuthors] = valueOfRandomElement;
            }
            while (countCities > 1)
            {
                countCities--;
                int randomPosition = rnd.Next(countCities + 1);
                string valueOfRandomElement = cities[randomPosition];
                cities[randomPosition] = cities[countCities];
                cities[countCities] = valueOfRandomElement;
            }
        }
    }
}
