using System;
using System.Collections.Generic;
using System.Linq;

namespace VehicleCatalogue
{
    class VehicleCatalogue
    {
        static void Main(string[] args)
        {
            string command = Console.ReadLine();
            Catalog carList = new Catalog();
            Catalog truckList = new Catalog();
            sbyte countOfCars = 0;
            sbyte countOfTrucks = 0;

            while (command != "End")
            {
                string[] currentVehicle = command.Split(" ");
                string type = currentVehicle[0];
                if(type == "car")
                {
                    countOfCars++;
                }
                else
                {
                    countOfTrucks++;
                }

                ListOfCarsAndTrucks(currentVehicle, type, carList, truckList);

                command = Console.ReadLine();
            }

            var listOfCars = new List<Car>();
            listOfCars = carList.Cars.ToList();

            var listOfTrucks = new List<Truck>();
            listOfTrucks = truckList.Trucks.ToList();
            command = Console.ReadLine();

            while (command != "Close the Catalogue")
            {
                string modelCommand = command;

                PrintTheListsByModels(command, listOfCars, listOfTrucks);
                command = Console.ReadLine();
            }

            CarAvarageHorsePower(listOfCars, countOfCars);
            TruckAvarageHorsePower(listOfTrucks, countOfTrucks);           
        }

        static void ListOfCarsAndTrucks(string[] currentVehicle,
            string type,
            Catalog carList,
            Catalog truckList)
        {
            if (type == "car")
            {
                string model = currentVehicle[1];
                string color = currentVehicle[2];
                short horsePower = short.Parse(currentVehicle[3]);

                Car vehicle = new Car()
                {
                    Type = type,
                    Model = model,
                    Color = color,
                    HorsePower = horsePower
                };

                carList.Cars.Add(vehicle);
            }
            else
            {
                string model = currentVehicle[1];
                string color = currentVehicle[2];
                short horsePower = short.Parse(currentVehicle[3]);

                Truck vehicle = new Truck()
                {
                    Type = type,
                    Model = model,
                    Color = color,
                    HorsePower = horsePower
                };

                truckList.Trucks.Add(vehicle);
            }
            
        }

        static void PrintTheListsByModels(string command,
            List<Car> listOfCars,
            List<Truck> listOfTrucks)
        {
            foreach (Car car in listOfCars)
            {
                if (command == car.Model)
                {
                    Console.WriteLine($"Type: Car");
                    Console.WriteLine($"Model: {car.Model}");
                    Console.WriteLine($"Color: {car.Color}");
                    Console.WriteLine($"Horsepower: {car.HorsePower}");
                }
            }

            foreach (Truck truck in listOfTrucks)
            {
                if (command == truck.Model)
                {
                    Console.WriteLine($"Type: Truck");
                    Console.WriteLine($"Model: {truck.Model}");
                    Console.WriteLine($"Color: {truck.Color}");
                    Console.WriteLine($"Horsepower: {truck.HorsePower}");
                }
            }
        }

        static void CarAvarageHorsePower(List<Car> listOfCars,
            sbyte countOfCars)
        {
            double averageSum = 0;
            int sum = 0;
            
            if(countOfCars > 0)
            {
                foreach (Car car in listOfCars)
                {
                    sum += car.HorsePower;
                }

                averageSum = (double)sum / countOfCars;
            }

            Console.WriteLine($"Cars have average horsepower of: {averageSum:F2}.");
        }

        static void TruckAvarageHorsePower(List<Truck> listOfTrucks,
            sbyte countOfTrucks)
        {
            double averageSum = 0;
            int sum = 0;
            
            if(countOfTrucks > 0)
            {
                foreach (Truck truck in listOfTrucks)
                {
                    sum += truck.HorsePower;
                }

                averageSum = (double)sum / countOfTrucks;
            }

            Console.WriteLine($"Trucks have average horsepower of: {averageSum:F2}.");
        }
    }
}
