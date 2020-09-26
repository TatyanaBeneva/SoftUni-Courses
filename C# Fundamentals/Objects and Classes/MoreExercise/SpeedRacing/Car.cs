using System;
using System.Collections.Generic;
using System.Text;

namespace SpeedRacing
{
    public class Car
    {
        public string model;
        public decimal fuelAmmount;
        public decimal fuelCost;
        public decimal distanceTravelled;

        public Car(string model, decimal fuelAmmount, decimal fuelCost)
        {
            this.model = model;
            this.fuelAmmount = fuelAmmount;
            this.fuelCost = fuelCost;
            this.distanceTravelled = 0;
        }

        public void Drive(decimal distance)
        {
            if (this.fuelAmmount < distance * this.fuelCost)
            {
                Console.WriteLine("Insufficient fuel for the drive");
            }
            else
            {
                this.fuelAmmount -= distance * this.fuelCost;
                this.distanceTravelled += distance;
            }
        }
    }
}
