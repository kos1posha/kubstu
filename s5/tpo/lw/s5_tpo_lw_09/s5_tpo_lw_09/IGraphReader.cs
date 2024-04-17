using System.IO;

namespace s5_tpo_lw_09;

public interface IGraphReader
{
    int[,] LoadEdgeList(TextReader reader);
}