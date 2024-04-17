using System.IO;
using s5_tpo_lw_09;

namespace s5_tpo_lw_09_tests;

public class DummyReader : IGraphReader
{
    public int[,] LoadEdgeList(TextReader reader)
    {
        return new[,]
        {
            { 0, 1, 0, 1 },
            { 1, 0, 1, 0 },
            { 0, 1, 0, 1 },
            { 1, 0, 1, 0 }
        };
    }
}