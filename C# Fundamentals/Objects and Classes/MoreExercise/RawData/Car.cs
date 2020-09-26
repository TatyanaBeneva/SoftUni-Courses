using System;
using System.Collections.Generic;
using System.Text;

namespace RawData
{
    class Car
    {
        public Car(string model, int engineSpeed, int enginePower, int cargoWeight, string cargoType)
        {
            Model = model;
            Engine = new Engine()
            {
                Speed = engineSpeed,
                Power = enginePower
            };
            Cargo = new Cargo()
            {
                Weight = cargoWeight,
                Type = cargoType
            };
        }

        public string Model { get; set; }

        public Engine Engine { get; set; }

        public Cargo Cargo { get; set; }
    }
}
