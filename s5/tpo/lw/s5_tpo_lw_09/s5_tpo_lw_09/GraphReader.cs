using System;
using System.IO;
using System.Linq;

namespace s5_tpo_lw_09;

public class GraphReader : IGraphReader
{
    public int[,] LoadEdgeList(TextReader reader)
    {
        int dims = Convert.ToInt32(reader.ReadLine());
        int[,] adjMat = new int[dims, dims];
        for (int i = 0; i < adjMat.GetLength(0); i++)
        for (int j = 0; j < adjMat.GetLength(1); j++)
            adjMat[i, j] = 0;

        while (reader.Peek() != -1)
        {
            try
            {
                string[] temp = reader.ReadLine()!.Split(' ').ToArray();
                adjMat[Convert.ToInt32(temp[0]) - 1, Convert.ToInt32(temp[1]) - 1] = 1;
                adjMat[Convert.ToInt32(temp[1]) - 1, Convert.ToInt32(temp[0]) - 1] = 1;
            }
            catch (FormatException e)
            {
                Console.WriteLine(e.Message);
                return null;
            }
            catch (ArgumentOutOfRangeException e)
            {
                Console.WriteLine(e.Message);
                return null;
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                return null;
            }
        }

        reader.Close();

        return adjMat;
    }
}