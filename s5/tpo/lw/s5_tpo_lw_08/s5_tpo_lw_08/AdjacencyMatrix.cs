namespace s5_tpo_lw_08;

public class AdjacencyMatrix : AdjacencyMatrixBase, IConvertibleTo<EdgeList>, IConvertibleTo<AdjacencyMatrix>
{
    public AdjacencyMatrix(int size) : base(size) { }
    public AdjacencyMatrix(double[,] data) : base(data) { }
    
    AdjacencyMatrix IConvertibleTo<AdjacencyMatrix>.Convert() => this;
    public EdgeList Convert()
    {
        EdgeList edgeList = new(Size);
        for (int i = 0; i < Size; i++)
        for (int j = i; j < Size; j++)
        {
            double distance = this[i, j];
            if (!double.IsInfinity(distance) && distance > 0)
                edgeList.Add((i, j), distance);
        }
        return edgeList;
    }
}