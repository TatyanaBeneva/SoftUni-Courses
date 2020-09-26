using System;
using System.Linq;
using System.Collections.Generic;

namespace Articles
{
    class Articles
    {
        static void Main(string[] args)
        {
            List<string> input = Console.ReadLine().Split(", ").ToList();
            int numOfCommands = int.Parse(Console.ReadLine());
            Article article = new Article();

            article.Title = input[0];
            article.Content = input[1];
            article.Author = input[2];

            for (int i = 0; i < numOfCommands; i++)
            {
                var command = Console.ReadLine().Split(": ").ToList();
                var changeWith = command[1];
                
                switch (command[0])
                {
                    case "Edit":
                        article.Edit(changeWith);
                        break;
                    case "ChangeAuthor":
                        article.ChangeAuthor(changeWith);
                        break;
                    case "Rename":
                        article.Rename(changeWith);
                        break;
                }
            }

            article.Result();
        }
    }
}
