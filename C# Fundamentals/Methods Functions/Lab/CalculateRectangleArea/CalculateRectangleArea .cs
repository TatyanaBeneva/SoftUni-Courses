using System;

namespace CalculateRectangleArea
{
    class CalculateRectangleArea
    {
        static void Main(string[] args)
        {
            int width = int.Parse(Console.ReadLine());
            int height = int.Parse(Console.ReadLine());
            int area = CalculateArea(width, height);
            Console.WriteLine(area);
        }

        static int CalculateArea(int width, int height)
        {
            return width * height;

        }
    }
}
