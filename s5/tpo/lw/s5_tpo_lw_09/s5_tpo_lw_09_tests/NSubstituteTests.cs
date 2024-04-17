using System.IO;
using NUnit.Framework;
using NSubstitute;
using FluentAssertions;
using s5_tpo_lw_09;

namespace s5_tpo_lw_09_tests;

public class NSubstitudeTests
{
    [Test]
    public void ConstructorTest()
    {
        DummyReader reader = new();
        DummyWriter writer = new();

        Graph graph = new(reader, writer);

        Assert.NotNull(graph);
    }

    [Test]
    public void LoadTest()
    {
        GraphReader reader = new();
        GraphWriter writer = new();

        StringReader readerString = new(
            "11\r\n1 2\r\n1 7\r\n2 3\r\n3 4\r\n3 5\r\n3 6\r\n7 8\r\n8 9\r\n8 10\r\n10 11\r\n9 11"
        );

        Graph graph = new(reader, writer);
        graph.ReadFromFile(readerString);

        int expected = 11;
        int actual = graph.AdjacencyMatrix.GetLength(0);

        Assert.AreEqual(expected, actual);
    }

    [Test]
    public void SaveTest()
    {
        GraphReader reader = new();
        GraphWriter writer = new();

        StringReader readerString = new(
            "11\r\n1 2\r\n1 7\r\n2 3\r\n3 4\r\n3 5\r\n3 6\r\n7 8\r\n8 9\r\n8 10\r\n10 11\r\n9 11"
        );
        StringWriter writerString = new();

        Graph graph = new(reader, writer);
        graph.ReadFromFile(readerString);
        graph.WriteToFile(writerString);

        string expected =
            "1 -> 2 -> 7\r\n2 -> 1 -> 3\r\n3 -> 2 -> 4 -> 5 -> 6\r\n4 -> 3\r\n5 -> 3\r\n6 -> 3\r\n7 -> 1 -> 8\r\n8 -> 7 -> 9 -> 10\r\n9 -> 8 -> 11\r\n10 -> 8 -> 11\r\n11 -> 9 -> 10\r\n";
        string actual = writerString.ToString();

        Assert.AreEqual(expected, actual);
    }
}

public class NSubstituteTests
{
    [Test]
    public void LoadTest()
    {
        IGraphReader reader = Substitute.For<IGraphReader>();
        IGraphWriter writer = Substitute.For<IGraphWriter>();

        StringReader stringReader = new("");

        Graph graph = new(reader, writer);
        reader.LoadEdgeList(stringReader).Returns(new[,]
        {
            { 0, 1, 0, 1 },
            { 1, 0, 1, 0 },
            { 0, 1, 0, 1 },
            { 1, 0, 1, 0 }
        });
        graph.ReadFromFile(stringReader);

        int expected = 4;
        int actual = graph.AdjacencyMatrix.GetLength(0);

        Assert.AreEqual(expected, actual);
    }
}

public class FluentAssertionsTests
{
    [Test]
    public void LoadTest()
    {
        GraphReader reader = new();
        GraphWriter writer = new();
        
        StreamReader stream = new("graph.txt");
        
        Graph graph = new(reader, writer);
        graph.ReadFromFile(stream);
        
        int[,] temp =
        {
            { 0, 1, 1, 1 },
            { 1, 0, 0, 1 },
            { 1, 0, 0, 1 },
            { 1, 1, 1, 0 }
        };
        
        graph.AdjacencyMatrix.GetLength(0).Should().Be(4);
        graph.AdjacencyMatrix.GetLength(1).Should().Be(4);
        
        for (int i = 0; i < graph.AdjacencyMatrix.GetLength(0); i++)
        for (int j = 0; j < graph.AdjacencyMatrix.GetLength(1); j++)
            graph.AdjacencyMatrix[i, j].Should().Be(temp[i, j]);
    }
}