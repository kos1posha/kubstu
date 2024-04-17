using System.Collections.Generic;
using System.IO;

namespace s5_tpo_lw_09;

public class GraphWriter : IGraphWriter
{
    public void SaveAdjacencyList(TextWriter writer, List<List<int>> list)
    {
        for (int i = 0; i < list.Count; i++)
        {
            writer.Write(i + 1);
            foreach (int item in list[i])
            {
                writer.Write(" -> " + (item + 1));
            }

            writer.WriteLine();
        }

        writer.Close();
    }
}