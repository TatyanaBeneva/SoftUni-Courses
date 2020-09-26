using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace WordSynonyms
{
    class WordSynonyms
    {
        static void Main(string[] args)
        {
            int numberOfPairs = int.Parse(Console.ReadLine());

            var wordSynonyms = new Dictionary<string, List<string>>();

            for(int i = 0; i < numberOfPairs; i++)
            {
                string word = Console.ReadLine();
                string synonym = Console.ReadLine();

                if (wordSynonyms.ContainsKey(word))
                {
                    List<string> list = wordSynonyms[word];
                    list.Add(synonym);
                }
                else
                {
                    wordSynonyms.Add(word, new List<string> { synonym });
                }
            }

            foreach(var word in wordSynonyms)
            {
                StringBuilder resulTextBuilder = new StringBuilder();

                resulTextBuilder.Append(word.Key);
                resulTextBuilder.Append(" - ");

                for(int i = 0; i < word.Value.Count; i++)
                {
                    resulTextBuilder.Append(word.Value[i]);

                    if(i != word.Value.Count - 1)
                    {
                        resulTextBuilder.Append(", ");
                    }
                }

                Console.WriteLine(resulTextBuilder);
            }
        }
    }
}
