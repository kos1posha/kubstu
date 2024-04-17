using System.Collections.Generic;
using System.IO;

namespace s5_tpo_lw_09;

public interface IGraphWriter
{
    void SaveAdjacencyList(TextWriter writer,
        List<List<int>> list);
}