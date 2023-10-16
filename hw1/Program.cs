using System.Reflection.PortableExecutable;
using System;
namespace hw1
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length > 0)
            {
                // проверка на первый элемент: число/не число
                if (!double.TryParse(args[0], out double num))
                {
                    System.Console.WriteLine($"Элемент {args[0]} не число");
                }
                double num1 = double.Parse(args[0]);
                double num2 = double.Parse(args[2]);
                if (args[1] == "+")
                {
                    System.Console.WriteLine(num1 + num2);
                }
                else if (args[1] == "-")
                {
                    System.Console.WriteLine(num1 - num2);
                }
                else if (args[1] == "/")
                {
                    System.Console.WriteLine(num1 / num2);
                }
                else if (args[1] == "*")
                { // умножение не считывает за символ умножения
                    /* dotnet run 1 * 2 
Unhandled exception. System.FormatException: The input string 'bin' was not in a correct format.
   at System.Number.ThrowOverflowOrFormatException(ParsingStatus status, ReadOnlySpan`1 value, TypeCode type)
   at System.Double.Parse(String s)
   at hw1.Program.Main(String[] args) in /Users/umpabook/src/C#/web1/1/hw1/Program.cs:line 17 */
                    System.Console.WriteLine(num1 * num2);
                }
            }
        }
    }
}
