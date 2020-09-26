using System;
using System.Collections.Generic;
using System.Linq;

namespace RawData
{
    class RawData
    {
        static void Main(string[] args)
        {
            int numOfLines = int.Parse(Console.ReadLine());
            List<Car> carList = new List<Car>();
            for(int i = 0; i < numOfLines; i++)
            {
                string[] input = Console.ReadLine().Split(" ");
                string model = input[0];
                int engineSpeed = int.Parse(input[1]);
                int enginePower = int.Parse(input[2]);
                int cargoWeight = int.Parse(input[3]);
                string cargoType = input[4];

                Car carInfo = new Car(model, engineSpeed, enginePower, cargoWeight, cargoType);
                carList.Add(carInfo);
            }

            string command = Console.ReadLine();
            List<string> orderedList = new List<string>();

            switch (command)
            {
                case "fragile":
                    FragileCommand(carList, orderedList);
                    break;
                case "flamable":
                    FlamableCommand(carList, orderedList);
                    break;
            }

            orderedList.Sort();

            Console.WriteLine(string.Join(Environment.NewLine, orderedList));

        }

        static void FragileCommand(List<Car> carList, List<string> orderedList)
        {
            foreach(Car car in carList)
            {
                if(car.Cargo.Type == "fragile" && car.Cargo.Weight < 1000)
                {
                    orderedList.Add(car.Model);
                }
            }
        }

        static void FlamableCommand(List<Car> carList, List<string> orderedList)
        {
            foreach (Car car in carList)
            {
                if (car.Cargo.Type == "flamable" && car.Engine.Power > 250)
                {
                    orderedList.Add(car.Model);
                }
            }
        }
    }
}
