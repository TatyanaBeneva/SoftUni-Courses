using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace LegendaryFarming
{
    class LegendaryFarming
    {
        static void Main(string[] args)
        {
            var legendaryItems = new Dictionary<string, int>();
            legendaryItems.Add("fragments", 0);
            legendaryItems.Add("motes", 0);
            legendaryItems.Add("shards", 0);

            var junkItems = new SortedDictionary<string, int>();
            int count = 0;

            while (true)
            {
                string[] items = Console.ReadLine().Split(" ");

                for (int i = 0; i < items.Length; i += 2)
                {
                    string material = items[i + 1].ToLower();
                    int quantity = int.Parse(items[i]);

                    if (legendaryItems.ContainsKey(material))
                    {
                        legendaryItems[material] += quantity;

                        legendaryItems.TryGetValue(material, out count);

                        if (count >= 250)
                        {
                            ObtainedMaterial(material);
                            legendaryItems[material] -= 250;
                            break;
                        }
                    }
                    else
                    {
                        AddJunkMaterials(junkItems, material, quantity);
                    }
                }

                if (count >= 250)
                {
                    break;
                }
            }

            legendaryItems = legendaryItems.OrderBy(o => o.Key)
                .OrderByDescending(o => o.Value)
                .ToDictionary(p => p.Key, p => p.Value);

            foreach (var legendary in legendaryItems)
            {
                Console.WriteLine($"{legendary.Key}: {legendary.Value}");
            }

            foreach (var junk in junkItems)
            {
                Console.WriteLine($"{junk.Key}: {junk.Value}");
            }
        }

        static void ObtainedMaterial(string material)
        {
            switch (material)
            {
                case "shards":
                    Console.WriteLine("Shadowmourne obtained!");
                    break;
                case "fragments":
                    Console.WriteLine("Valanyr obtained!");
                    break;
                case "motes":
                    Console.WriteLine("Dragonwrath obtained!");
                    break;
            }
        }

        static void AddJunkMaterials(SortedDictionary<string, int> junkItems, string material, int quantity)
        {
            if (junkItems.ContainsKey(material))
            {
                junkItems[material] += quantity;
            }
            else
            {
                junkItems.Add(material, quantity);
            }
        }
    }
}
