namespace s5_tpo_lw_08;

public class DummyAMReader: IGraphReader<AdjacencyMatrix>
{
    public AdjacencyMatrix Read(string path)
    {
        double inf = double.PositiveInfinity;
        return new AdjacencyMatrix(new[,] 
        {
            { 0,   40, inf, inf,  18 },
            { 40,   0,  22,   6,  15 },
            { inf, 22,   0,  14, inf },
            { inf,  6,  14,   0,  20 },
            { 18,  15, inf,  20,   0 }
        });
    }
}