using System;
using System.Linq;
using System.Collections.Generic;

namespace Articles2
{
    class Articles2
    {
        static void Main(string[] args)
        {
            int numOfArticles = int.Parse(Console.ReadLine());
            var listOfArticles = new List<Article>();

            for (int i = 0; i < numOfArticles; i++)
            {
                string[] input = Console.ReadLine().Split(", ");
                string title = input[0];
                string content = input[1];
                string author = input[2];
                Article article = new Article()
                {
                    Title = title,
                    Content = content,
                    Author = author
                };

                listOfArticles.Add(article);
            }

            string orderTo = Console.ReadLine();

            PrintTheOrderedList(listOfArticles, orderTo);
        }

        static void PrintTheOrderedList(List<Article> listOfArticles, string orderTo)
        {
            var orderedList = new List<Article>();

            switch (orderTo)
            {
                case "title":
                    orderedList = listOfArticles.OrderBy(o => o.Title).ToList();
                    break;
                case "content":
                    orderedList = listOfArticles.OrderBy(o => o.Content).ToList();
                    break;
                case "author":
                    orderedList = listOfArticles.OrderBy(o => o.Author).ToList();
                    break;
            }

            foreach(Article article in orderedList)
            {
                Console.WriteLine($"{article.Title} - {article.Content}: {article.Author}");
            }
        }
    }
}
