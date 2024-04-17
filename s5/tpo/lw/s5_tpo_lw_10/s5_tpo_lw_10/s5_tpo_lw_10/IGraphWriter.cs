using System.Collections.Generic;

namespace s5_tpo_lw_10;

public interface IGraphWriter
{
    void SaveGraph(string path, Dictionary<int, List<int>> adjacencyMatrix);
}