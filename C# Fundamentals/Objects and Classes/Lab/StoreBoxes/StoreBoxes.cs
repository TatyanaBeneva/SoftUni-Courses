using System;
using System.Collections.Generic;
using System.Linq;

namespace StoreBoxes
{
    class StoreBoxes
    {
        static void Main(string[] args)
        {
            var itemInformationList = new List<Box>();
            string command = Console.ReadLine();

            while(command != "end")
            {
                string[] currentItem = command.Split(" ");

                string serialNum = currentItem[0];
                string itemName = currentItem[1];
                int itemQuantity = int.Parse(currentItem[2]);
                double itemPrice = double.Parse(currentItem[3]);

                Box itemInformation = new Box();
                itemInformation.Item = new Item();
                itemInformation.SerialNumber = serialNum;
                itemInformation.Item.Name = itemName;
                itemInformation.ItemQuantity = itemQuantity;
                itemInformation.Item.Price = itemPrice;
                itemInformation.PriceBox = (decimal)((double)itemQuantity * itemPrice);

                itemInformationList.Add(itemInformation);

                command = Console.ReadLine();
            }

            var sortedList = new List<Box>();
            sortedList = itemInformationList.OrderBy(o => o.PriceBox).ToList();
            sortedList.Reverse();

            foreach(Box item in sortedList)
            {
                Console.WriteLine($"{item.SerialNumber}\n" +
                    $"-- {item.Item.Name} - ${item.Item.Price:F2}: {item.ItemQuantity}\n-- ${item.PriceBox:F2}");
            }
        }
    }
}
