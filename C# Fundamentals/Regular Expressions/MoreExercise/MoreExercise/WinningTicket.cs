using System;
using System.Linq;
using System.Text.RegularExpressions;

class WinningTicket
{
    static void Main()
    {
        var regex = new Regex(@"@{6,}|\${6,}|#{6,}|\^{6,}");

        var tickets = Console.ReadLine().Split(',').Select(x => x.Trim()).ToArray();

        foreach (var ticket in tickets)
        {
            if (ticket.Length != 20)
            {
                Console.WriteLine("invalid ticket");
                continue;
            }

            var leftSide = ticket.Substring(0, 10); //Взимаме първата половина
            var matchLeft = regex.Match(leftSide); //Проверяваме за съвпадение в нея
            var rightSide = ticket.Substring(10, 10);//Взимаме втората половина
            var matchRight = regex.Match(rightSide);//Проверяваме за съвпадение в нея

            if ((matchLeft.Success && matchRight.Success && matchLeft.Value[0] == matchRight.Value[0]))
            {
                var winningString = Math.Min(matchLeft.Value.Length, matchRight.Value.Length);//Дължина на печелившата линия
                var winningSymbol = matchLeft.Value[0];//Печеливш символ
                if (winningString == 10) //Отпечатване на джакпот
                {
                    Console.WriteLine($@"ticket ""{ticket}"" - {winningString}{winningSymbol} Jackpot!");
                }
                else //Отпечатване за обикновен печеливш билет
                {
                    Console.WriteLine($@"ticket ""{ticket}"" - {winningString}{winningSymbol}");
                }
            }
            else
            {
                Console.WriteLine($@"ticket ""{ticket}"" - no match");
            }
        }
    }
}

//using System;
//using System.Text.RegularExpressions;

//namespace WinningTicket
//{
//    class WinningTicket
//    {
//        static void Main(string[] args)
//        {
//            string[] input = Console.ReadLine().Split(new char[] { ',', ' ' }, StringSplitOptions.RemoveEmptyEntries);

//            foreach(string current in input)
//            {
//                if(IsTicketValid(current) == false)
//                {
//                    Console.WriteLine("invalid ticket");
//                }
//                else
//                {
//                    TicketMatch(current);
//                }
//            }
//        }

//        static void TicketMatch(string current)
//        {
//            string regex = @"(([a-zA-Z]+)([@|#|\^|\$]+)([a-zA-Z]+)\3([a-zA-Z]+))|(([@|#|\^|\$]+))";
//            Match matches = Regex.Match(current, regex);
//            if (matches.Success)
//            {
//                int countLeft = 0;
//                int countRight = 0;
//                char simbol = ' ';

//                for(int i = 0; i < current.Length/2; i++)
//                {
//                    switch (current[i])
//                    {
//                        case '@': 
//                        case '$':
//                        case '^':
//                        case '#':
//                            countLeft++;
//                            simbol = current[i];
//                            break;
//                    }
//                }

//                for(int i = current.Length - 1; i >= current.Length/2; i--)
//                {
//                    switch (current[i])
//                    {
//                        case '@':
//                        case '$':
//                        case '^':
//                        case '#':
//                            countRight++;
//                            break;
//                    }
//                }

//                if(countRight >= 6 && countRight < 10 && countLeft >= 6 && countLeft < 10)
//                {
//                    if(countLeft < countRight)
//                    {
//                        Console.WriteLine($"ticket \"{current}\" - {countLeft}{simbol}");
//                    }
//                    else
//                    {
//                        Console.WriteLine($"ticket \"{current}\" - {countRight}{simbol}");
//                    }
//                }
//                else if(countRight == countLeft && countRight == 10)
//                {
//                    Console.WriteLine($"ticket \"{current}\" - 10{simbol} Jackpot!");
//                }
//            }
//            else
//            {
//                Console.WriteLine($"ticket \"{current}\" - no match");
//            }
//        }

//        static bool IsTicketValid(string current)
//        {
//            if(current.Length == 20)
//            {
//                return true;
//            }

//            return false;
//        }
//    }
//}
