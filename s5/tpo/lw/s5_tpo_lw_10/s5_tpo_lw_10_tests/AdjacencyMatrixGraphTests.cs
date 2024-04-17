using System;
using System.Collections.Generic;
using NUnit.Framework;
using s5_tpo_lw_10;
using FluentAssertions;


namespace s5_tpo_lw_10_tests;

[TestFixture]
public class AdjacencyMatrixGraphTests
{
    [Test]
    public void NotConnectedGraphTest()
    {
        Graph graph = new(new ReaderStubNotConnected(), new WriterDummy());
        graph.AdjacencyMatrix.Should().BeNull();
        graph.ReadFromFile("");
        graph.AdjacencyMatrix.Should().NotBeNull();
    }

    [Test]
    public void ConnectedGraphTest()
    {
        Graph graph = new(new ReaderStubConnected(), new WriterDummy());
        Action graphIsConnected = () => graph.IsConnected();
        graphIsConnected.Should().Throw<NullReferenceException>();
        graph.ReadFromFile("");
        graph.IsConnected().Should().BeTrue();
    }

    [Test]
    public void NullEdge1GraphTest()
    {
        Graph graph = new(new ReaderStubNullEdge1(), new WriterDummy());
        Action readNullEdgeGraph = () => graph.ReadFromFile("");
        readNullEdgeGraph.Should().Throw<ArgumentException>().WithMessage("Incidence matrix is invalid");
    }

    [Test]
    public void NullEdge2GraphTest()
    {
        Graph graph = new(new ReaderStubNullEdge2(), new WriterDummy());
        Action readNullEdgeGraph = () => graph.ReadFromFile("");
        readNullEdgeGraph.Should().Throw<ArgumentException>().WithMessage("Incidence matrix is invalid");
    }

    [Test]
    public void AdjacencyListGraphTest()
    {
        Graph graph = new(new ReaderStubNotConnected(), new WriterDummy());
        graph.ReadFromFile("");

        Dictionary<int, List<int>> actual = graph.GetAdjacencyList();
        Dictionary<int, List<int>> expected = new()
        {
            { 0, new List<int> { 3 } },
            { 1, new List<int> { 2 } },
            { 2, new List<int> { 1, 4 } },
            { 3, new List<int> { 0 } },
            { 4, new List<int> { 2 } }
        };

        actual.Should().BeEquivalentTo(expected);
    }
}