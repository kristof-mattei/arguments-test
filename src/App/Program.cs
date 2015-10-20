namespace App
{
    using System;

    internal static class Program
    {
        private static void Main(string[] args)
        {
            foreach (var arg in args)
            {
                Console.WriteLine(arg);
            }

            Console.WriteLine("All done");
            Console.ReadLine();
        }
    }
}