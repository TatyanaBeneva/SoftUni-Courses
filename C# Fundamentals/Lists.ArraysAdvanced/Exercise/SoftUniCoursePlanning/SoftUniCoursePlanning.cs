using System;
using System.Linq;
using System.Collections.Generic;

namespace SoftUniCoursePlanning
{
    class SoftUniCoursePlanning
    {
        static void Main(string[] args)
        {
            List<string> schedule = Console.ReadLine().Split(", ").ToList();
            string endCommand = Console.ReadLine();

            while(endCommand != "course start")
            {
                List<string> commands = endCommand.Split(":").ToList();

                switch (commands[0])
                {
                    case "Add":
                        Add(schedule, commands);
                        break;
                    case "Insert":
                        Insert(schedule, commands);
                        break;
                    case "Remove":
                        Remove(schedule, commands);
                        break;
                    case "Swap":
                        Swap(schedule, commands);
                        break;
                    case "Exercise":
                        Exercise(schedule, commands);
                        break;
                }

                endCommand = Console.ReadLine();
            }
            for(int i = 0; i < schedule.Count; i++)
            {
                schedule[i] = $"{i + 1}.{schedule[i]}";
            }
            Console.WriteLine(string.Join("\n", schedule));
        }

        static void Add(List<string> schedule, List<string> commands)
        {
            if (schedule.Contains(commands[1]) == false)
            {
                schedule.Add(commands[1]);
            }
            else
            {
                return;
            }
        }

        static void Insert(List<string> schedule, List<string> commands)
        {
            int index = int.Parse(commands[2]);
            if (schedule.Contains(commands[1]) == false)
            {
                schedule.Insert(index, commands[1]);
            }
            else
            {
                return;
            }
        }

        static void Remove(List<string> schedule, List<string> commands)
        {
            if (schedule.Contains(commands[1]))
            {
                schedule.Remove(commands[1]);
            }
            else
            {
                return;
            }
        }

        static void Swap(List<string> schedule, List<string> commands)
        {
            if (schedule.Contains(commands[1]) && schedule.Contains(commands[2]))
            {
                int indexAtFirstLesson = schedule.IndexOf(commands[1]);
                int indexAtSecondLesson = schedule.IndexOf(commands[2]);
                string firstLesson = commands[1];
                string secondLesson = commands[2];
                schedule.Insert(indexAtFirstLesson, secondLesson);
                schedule.RemoveAt(indexAtFirstLesson + 1);
                schedule.Insert(indexAtSecondLesson, firstLesson);
                schedule.RemoveAt(indexAtSecondLesson + 1);

                if (schedule.Contains($"{firstLesson}-Exercise"))
                {
                    schedule.Remove($"{firstLesson}-Exercise");
                    schedule.Insert(schedule.IndexOf(commands[1]) + 1, $"{firstLesson}-Exercise");
                }
                if (schedule.Contains($"{secondLesson}-Exercise"))
                {
                    schedule.Remove($"{secondLesson}-Exercise");
                    schedule.Insert(schedule.IndexOf(commands[2]) + 1, $"{secondLesson}-Exercise");
                }
            }
            else
            {
                return;
            }
        }

        static void Exercise(List<string> schedule, List<string> commands)
        {
            if(schedule.Contains(commands[1]) == true && schedule.Contains($"{commands[1]}-Exercise") == false)
            {
                int lessonIndex = schedule.IndexOf(commands[1]);
                schedule.Insert(lessonIndex + 1, $"{commands[1]}-Exercise");
            }
            else if(schedule.Contains(commands[1]) == false && schedule.Contains($"{commands[1]}-Exercise") == false)
            {
                schedule.Add(commands[1]);
                schedule.Add($"{commands[1]}-Exercise");
            }
            else
            {
                return;
            }
        }
    }
}
