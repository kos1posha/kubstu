using s5_tpo_lw_10;

namespace s5_tpo_lw_10_tests;

public class ReaderStubNotConnected : IGraphReader
{
    public int[,] LoadGraph(string path)
    {
        return new[,]
        {
            { 0, 0, 1 },
            { 1, 0, 0 },
            { 1, 1, 0 },
            { 0, 0, 1 },
            { 0, 1, 0 }
        };
    }
}