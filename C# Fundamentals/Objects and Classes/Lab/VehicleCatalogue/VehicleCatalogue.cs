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


            while (command != "end")
            {
                string[] currentVehicle = command.Split("/");
                string type = currentVehicle[0];

                ListOfCarsAndTrucks(currentVehicle, type, carList, truckList);
                
                command = Console.ReadLine();
            }

            var sortedListOfCars = new List<Car>();
            sortedListOfCars = carList.Cars.OrderBy(o => o.Brand).ToList();

            var sortedListOfTrucks = new List<Truck>();
            sortedListOfTrucks = truckList.Trucks.OrderBy(o => o.Brand).ToList();

            PrintTheResult(sortedListOfCars, sortedListOfTrucks);
        }

        static void ListOfCarsAndTrucks(string[] currentVehicle, string type, Catalog carList, Catalog truckList)
        {
            if (type == "Car")
            {
                string brand = currentVehicle[1];
                string model = currentVehicle[2];
                int horsePower = int.Parse(currentVehicle[3]);

                Car vehicle = new Car();
                vehicle.Brand = brand;
                vehicle.Model = model;
                vehicle.HorsePower = horsePower;

                carList.Cars.Add(vehicle);
            }
            else
            {
                string brand = currentVehicle[1];
                string model = currentVehicle[2];
                int weight = int.Parse(currentVehicle[3]);

                Truck vehicle = new Truck();
                vehicle.Brand = brand;
                vehicle.Model = model;
                vehicle.Weight = weight;

                truckList.Trucks.Add(vehicle);
            }
        }

        static void PrintTheResult(List<Car> sortedListOfCars, List<Truck> sortedListOfTrucks)
        {
            Console.WriteLine("Cars:");
            foreach (Car car in sortedListOfCars)
            {
                Console.WriteLine($"{car.Brand}: {car.Model} - {car.HorsePower}hp");
            }
            Console.WriteLine("Trucks:");
            foreach (Truck truck in sortedListOfTrucks)
            {
                Console.WriteLine($"{truck.Brand}: {truck.Model} - {truck.Weight}kg");
            }
        }
    }
}
