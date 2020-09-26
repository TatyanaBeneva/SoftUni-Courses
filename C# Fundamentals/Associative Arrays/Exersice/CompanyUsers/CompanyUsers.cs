using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CompanyUsers
{
    class CompanyUsers
    {
        static void Main(string[] args)
        {
            var listOfCompany = new SortedDictionary<string, List<string>>();

            while (true)
            {
                string command = Console.ReadLine();

                if(command == "End")
                {
                    break;
                }
                else
                {
                    string[] currentInfo = command.Split(" -> ");

                    AddInfo(listOfCompany, currentInfo);
                }
            }

            foreach(var company in listOfCompany)
            {
                Console.WriteLine(company.Key);

                foreach(var list in company.Value)
                {
                    Console.WriteLine($"-- {list}");
                }
            }
        }

        static void AddInfo(SortedDictionary<string, List<string>> listOfCompany, string[] currentInfo)
        {
            if(IsCompanyExist(listOfCompany, currentInfo) == true)
            {
                if (IsEmployeExist(listOfCompany, currentInfo) == false)
                {
                    List<string> list = listOfCompany[currentInfo[0]];
                    list.Add(currentInfo[1]);
                }
            }
            else
            {
                listOfCompany.Add(currentInfo[0], new List<string> { currentInfo[1] });
            }
        }

        static bool IsCompanyExist(SortedDictionary<string, List<string>> listOfCompany, string[] currentInfo)
        {
            if (listOfCompany.ContainsKey(currentInfo[0]))
            {
                return true;
            }

            return false;
        }

        static bool IsEmployeExist(SortedDictionary<string, List<string>> listOfCompany, string[] currentInfo)
        {
            if (listOfCompany[currentInfo[0]].Contains(currentInfo[1]))
            {
                return true;
            }

            return false;
        }
    }
}
