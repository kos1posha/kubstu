using System.Collections.Generic;

namespace s5_tpo_lw_08;

public class EdgeList : EdgeListBase, IConvertibleTo<EdgeList>, IConvertibleTo<AdjacencyMatrix>
{
    public EdgeList(int size) : base(size) { }
    public EdgeList(Dictionary<(int from, int to), double> data) : base(data) { }
    public EdgeList(Dictionary<(int from, int to), double> data, int size) : base(data, size) { }
    
    EdgeList IConvertibleTo<EdgeList>.Convert() => this;
    public AdjacencyMatrix Convert()
    {
        AdjacencyMatrix adjacencyMatrix = new(Size);
        foreach (KeyValuePair<(int from, int to), double> edge in _data)
            adjacencyMatrix[edge.Key.from, edge.Key.to] = edge.Key.from != edge.Key.to && edge.Value == 0
                ? double.PositiveInfinity : edge.Value;
        for (int i = 0; i < Size; i++) for (int j = i + 1; j < Size; j++)
            if (adjacencyMatrix[i, j] == 0)
                adjacencyMatrix[i, j] = double.PositiveInfinity;
        return adjacencyMatrix;
    }
    
    public double FindShortestPath(int from, int to)
    {
        // TODO Implement this
        return 0;
    }
}