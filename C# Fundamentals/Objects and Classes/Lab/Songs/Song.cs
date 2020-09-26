using System;
using System.Collections.Generic;
using System.Text;

namespace Songs
{
    class Song
    {
        public Song()
        {

        }

        public string GetTypeAndName()
        {
            return $"{TypeList} {Name}";
        }

        public string TypeList { get; set; }

        public string Name { get; set; }

        public string Time { get; set; }
    }
}
