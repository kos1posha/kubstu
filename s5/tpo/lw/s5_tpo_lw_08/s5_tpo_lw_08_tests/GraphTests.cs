using System;
using NUnit.Framework;
using s5_tpo_lw_08;

namespace s5_tpo_lw_08_tests;

[TestFixture]
public class GraphTests
{
    readonly double inf = double.PositiveInfinity;

    public Graph<AdjacencyMatrix, EdgeList, AdjacencyMatrix> InitTestGraph()
    {
        IGraphReader<EdgeList> reader = new DummyELReader();
        IGraphWriter<AdjacencyMatrix> writer = new DummyAMWriter();
        return new Graph<AdjacencyMatrix, EdgeList, AdjacencyMatrix>(reader, writer);
    }

    [Test]
    public void ReadGraphFromFileTest()
    {
        Graph<AdjacencyMatrix, EdgeList, AdjacencyMatrix> graph = InitTestGraph();
        graph.ReadFromFile("read.txt");
        double[,] expected =
        {
            { 0, 40, inf, inf, 18 },
            { 40, 0, 22, 6, 15 },
            { inf, 22, 0, 14, inf },
            { inf, 6, 14, 0, 20 },
            { 18, 15, inf, 20, 0 }
        };

        Assert.AreEqual(expected.GetLength(0), graph.Representation.Size);
        for (int i = 0; i < graph.Representation.Size; i++)
        for (int j = 0; j < graph.Representation.Size; j++)
            Assert.AreEqual(expected[i, j], graph.Representation[i, j]);
    }

    [Test]
    public void WriteGraphToFileTest()
    {
        Graph<AdjacencyMatrix, EdgeList, AdjacencyMatrix> graph = InitTestGraph();
        graph.ReadFromFile("read.txt");
        bool isWritten = graph.WriteToFile("write.txt");
        Assert.AreEqual(true, isWritten);
    }

    [Test]
    public void WriteNullGraphToFileTest()
    {
        Graph<AdjacencyMatrix, EdgeList, AdjacencyMatrix> graph = InitTestGraph();
        Assert.Catch<NullReferenceException>(() => { graph.WriteToFile("write.txt"); });
    }
}