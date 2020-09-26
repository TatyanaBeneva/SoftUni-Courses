using System;
using System.Collections.Generic;

namespace Songs
{
    class Songs
    {
        static void Main(string[] args)
        {
            int numberOfSongs = int.Parse(Console.ReadLine());
            var songList = new List<Song>();

            for(int i = 0; i < numberOfSongs; i++)
            {
                string[] currentSong = Console.ReadLine().Split("_");
                Song song = new Song();
                song.TypeList = currentSong[0];
                song.Name = currentSong[1];
                song.Time = currentSong[2];

                songList.Add(song);
            }

            string typeList = Console.ReadLine();

            if(typeList == "all")
            {
                foreach(Song song in songList)
                {
                    Console.WriteLine(song.Name);
                }
            }
            else
            {
                foreach(Song song in songList)
                {
                    if(song.TypeList == typeList)
                    {
                        Console.WriteLine(song.Name);
                    }
                }
            }
        }
    }
}
