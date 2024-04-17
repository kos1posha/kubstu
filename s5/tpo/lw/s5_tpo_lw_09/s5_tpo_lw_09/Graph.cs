using System;
using System.Collections.Generic;
using System.IO;

namespace s5_tpo_lw_09;

public class Graph
{
    public IGraphReader Reader { get; set; }
    public IGraphWriter Writer { get; set; }

    public int[,] AdjacencyMatrix;

    public Graph(IGraphReader reader, IGraphWriter writer)
    {
        Reader = reader;
        Writer = writer;
        AdjacencyMatrix = null;
    }

    public void ReadFromFile(TextReader textReader)
    {
        AdjacencyMatrix = Reader.LoadEdgeList(textReader);
        if (AdjacencyMatrix == null)
        {
            throw new Exception("Некорректный формат файла");
        }
    }

    public void WriteToFile(TextWriter textWriter)
    {
        List<List<int>> adjList = new(AdjacencyMatrix.GetLength(0));

        for (int i = 0; i < AdjacencyMatrix.GetLength(0); i++)
            adjList.Add(new List<int>());

        for (int i = 0; i < AdjacencyMatrix.GetLength(0); i++)
        for (int j = 0; j < AdjacencyMatrix.GetLength(1); j++)
            if (AdjacencyMatrix[i, j] != 0)
                adjList[i].Add(j);

        Writer.SaveAdjacencyList(textWriter, adjList);
    }

    public void DFS(int start)
    {
        bool[] visited = new bool[AdjacencyMatrix.GetLength(0)];
        this.DFS(--start, visited);
    }

    private void DFS(int start, bool[] visited)
    {
        Console.Write($"{start + 1} ");

        visited[start] = true;
        for (int i = 0; i < AdjacencyMatrix.GetLength(0); i++)
            if (AdjacencyMatrix[start, i] == 1 && (!visited[i]))
                DFS(i, visited);
    }
}