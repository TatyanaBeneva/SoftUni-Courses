using System;
using System.Collections.Generic;
using System.Text;

namespace Articles
{
    class Article
    {
        public Article()
        {

        }

        public string Title { get; set; }

        public string Content { get; set; }

        public string Author { get; set; }

        public void Edit(string changeWith)
        {
            Content = changeWith;
        }

        public void ChangeAuthor(string changeWith)
        {
                Author = changeWith;          
        }

        public void Rename(string changeWith)
        {

            Title = changeWith;
        }

        public void Result()
        {
            Console.WriteLine($"{Title} - {Content}: {Author}");
        }
    }
}
