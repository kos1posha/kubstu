using System;
using System.Collections.Generic;

namespace s5_tpo_lw_08;

internal static class Program
{
    public static void TestRepresentations()
    {
        AdjacencyMatrix amRead = new DummyAMReader().Read("");
        Console.WriteLine(amRead);
        EdgeList elRead = new DummyELReader().Read("");
        Console.WriteLine(elRead);

        Console.WriteLine();

        AdjacencyMatrix amConvert = elRead.Convert();
        Console.WriteLine(amConvert);
        EdgeList elConvert = amRead.Convert();
        Console.WriteLine(elConvert);
    }

    public static void TestGraph()
    {
        IGraphReader<AdjacencyMatrix> reader = new DummyAMReader();
        IGraphWriter<AdjacencyMatrix> writer = new DummyAMWriter();
        Graph<EdgeList, AdjacencyMatrix, AdjacencyMatrix> graph = new(reader, writer);
        graph.ReadFromFile("");
        Console.WriteLine(graph);
    }

    public static void TestFSP()
    {
        EdgeList el = new DummyELReader().Read("");
        double shortestPath = el.FindShortestPath(5, 3);
        Console.WriteLine(shortestPath);
    }

    public static EdgeList WikiMatrix =>
        new EdgeList(new Dictionary<(int from, int to), double>
        {
            { (0, 1),  7 },
            { (0, 2),  9 },
            { (0, 5), 14 },
            { (1, 2), 10 },
            { (1, 3), 15 },
            { (2, 3), 11 },
            { (2, 5),  2 },
            { (3, 4),  6 },
            { (4, 5),  9 }
        });

    static void Main()
    {
        Console.WriteLine(WikiMatrix.FindShortestPath(0, 4));

    }
}