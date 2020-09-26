using System;

public class Program
{
    public static void Main()
    {
        string input = Console.ReadLine();
        string[] divided = input.Split('>');

        int explosionStrength = 0;
        int remainingExplosionStrength = 0;
        for (int i = 1; i < divided.Length; i++)
        {
            explosionStrength = int.Parse("" + divided[i][0]) + remainingExplosionStrength;
            remainingExplosionStrength = explosionStrength - divided[i].Length;

            if (explosionStrength > divided[i].Length)
                explosionStrength = divided[i].Length;

            divided[i] = divided[i].Substring(explosionStrength);
            if (remainingExplosionStrength < 0)
                remainingExplosionStrength = 0;
        }

        String result = String.Join(">", divided);
        Console.WriteLine(result);
    }
}

//using System;
//using System.Collections.Generic;
//using System.Linq;

//namespace StringExplosion
//{
//    class StringExplosion
//    {
//        static void Main(string[] args)
//        {
//            string text = Console.ReadLine();
//            int prevCount = 0;

//            for(int i = 0; i < text.Length; i++)
//            {
//                if(text[i] == '>')
//                {
//                    string digitInString =text[i + 1].ToString();
//                    int digit = int.Parse(digitInString) + prevCount;

//                    if(text.Length - 1 >= i + digit)
//                    {
//                        if(digit > 0)
//                        {
//                            if (text[i + 2] != '>')
//                            {
//                                text = text.Remove(i + 1, digit);
//                                prevCount = 0;
//                            }
//                            else
//                            {
//                                text = text.Remove(i + 1, 1);
//                                prevCount += digit - 1;
//                            }
//                        }
//                        else
//                        {
//                            text = text.Remove(i + 1, 1);
//                        }
//                    }
//                    else
//                    {
//                        text = text.Remove(i + 1);
//                    }
//                }
//            }

//            Console.WriteLine(text);
//        }
//    }
//}
