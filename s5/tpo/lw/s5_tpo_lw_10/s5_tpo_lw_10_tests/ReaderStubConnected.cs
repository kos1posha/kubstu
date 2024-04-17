using s5_tpo_lw_10;

namespace s5_tpo_lw_10_tests;

public class ReaderStubConnected : IGraphReader
{
    public int[,] LoadGraph(string path)
    {
        return new[,]
        {
            { 0, 0, 1, 1 },
            { 1, 0, 0, 1 },
            { 1, 1, 0, 0 },
            { 0, 0, 1, 0 },
            { 0, 1, 0, 0 }
        };
    }

    calculator.Add(10, -5);
    calculator.Received().Add(10, Arg.Any<int>());
    calculator.Received().Add(10, Arg.Is<int>(x => x < 0));
}