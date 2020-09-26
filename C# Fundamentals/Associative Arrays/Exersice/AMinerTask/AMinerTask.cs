using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AMinerTask
{
    class AMinerTask
    {
        static void Main(string[] args)
        {
            var resources = new Dictionary<string, int>();
            string command = Console.ReadLine();

            while (true)
            {
                if(command == "stop")
                {
                    break;
                }

                string resource = command;
                int quantity = int.Parse(Console.ReadLine());

                if (resources.ContainsKey(resource))
                {
                    resources[resource] += quantity;
                }
                else
                {
                    resources.Add(resource, quantity);
                }

                command = Console.ReadLine();
            }

            foreach(var resource in resources)
            {
                Console.WriteLine($"{resource.Key} -> {resource.Value}");
            }
        }
    }
}
