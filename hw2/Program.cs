using System;

namespace hw2;

class Program
{
    public void Output(int[,] arr)
    {
        for (int i = 0; i < arr.GetLength(0); i++)
        {
            for (int j = 0; j < arr.GetLength(1); j++)
            {
                System.Console.Write(arr[i, j] + " ");
            }
            System.Console.WriteLine();
        }
    }

    public int[] Sort(int[,] arr)
    {
        int[] temp = new int[arr.GetLength(0) * arr.GetLength(1)];

        for (int i = 0; i < arr.GetLength(0); i++)
        {
            for (int j = 0; j < arr.GetLength(1); j++)
            {
                temp[i * arr.GetLength(1) + j] = arr[i, j];
            }
        }

        for (int i = 0; i < temp.Length; i++)
        {
            for (int j = 0; j < temp.Length - i - 1; j++)
            {
                if (temp[j] > temp[j + 1])
                {
                    int ttemp = temp[j + 1];
                    temp[j + 1] = temp[j];
                    temp[j] = ttemp;
                }
            }
        }
        return temp;
    }
    public void NewOutput(int[,] arr, int[] temp)
    {
        int rows = arr.GetUpperBound(0) + 1;    // количество строк
        int columns = arr.Length / rows;        // количество столбцов

        int index = 0;
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < columns; j++)
            {
                arr[i, j] = temp[index];
                index++;
            }
        }

        // Вывод многомерного массива
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < columns; j++)
            {
                Console.Write(arr[i, j] + " ");
            }
            Console.WriteLine();
        }
    }
    static void Main(string[] args)
    {
        Program pr = new Program();
        int[,] arr = new int[,] { { 7, 8, 9 }, { 4, 5, 6 }, { 1, 2, 3 } };
        pr.Output(arr);
        int[] temp = pr.Sort(arr);
        System.Console.WriteLine();
        pr.NewOutput(arr, temp);
    }
}