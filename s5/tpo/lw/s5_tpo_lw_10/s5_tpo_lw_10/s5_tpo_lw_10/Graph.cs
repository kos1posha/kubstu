using System;
using System.Collections.Generic;

namespace s5_tpo_lw_10;

public class Graph
{
    private int[,] adjacencyMatrix;

    public int[,] AdjacencyMatrix
    {
        get => adjacencyMatrix;
        set => adjacencyMatrix = value;
    }

    public IGraphReader Reader { get; set; }
    public IGraphWriter Writer { get; set; }

    public Graph(IGraphReader reader, IGraphWriter writer)
    {
        Reader = reader;
        Writer = writer;
        adjacencyMatrix = null;
    }

    public Graph(IGraphReader reader, IGraphWriter writer, int[,] adjacencyMatrix) : this(reader, writer)
    {
        this.adjacencyMatrix = adjacencyMatrix;
    }

    public void ReadFromFile(string path)
    {
        int[,] incidenceMatrix = Reader.LoadGraph(path);
        List<int> edge = new();

        adjacencyMatrix = new int[incidenceMatrix.GetLength(0), incidenceMatrix.GetLength(0)];
        for (int j = 0; j < incidenceMatrix.GetLength(1); j++)
        {
            edge.Clear();
            for (int i = 0; i < incidenceMatrix.GetLength(0); i++)
                if (incidenceMatrix[i, j] == 1)
                    edge.Add(i);

            if (edge.Count is not (0 or 2)) throw new ArgumentException("Incidence matrix is invalid");
            if (edge.Count != 2) continue;
            adjacencyMatrix[edge[0], edge[1]] = 1;
            adjacencyMatrix[edge[1], edge[0]] = 1;
        }
    }

    public void WriteToFile(string path)
    {
        Writer.SaveGraph(path, GetAdjacencyList());
    }

    public bool IsConnected()
    {
        int[,] distance = FloydWarshall();

        for (int i = 0; i < distance.GetLength(0); i++)
        for (int j = 0; j < distance.GetLength(0); j++)
            if (distance[i, j] == int.MaxValue)
                return false;

        return true;
    }

    public int[,] FloydWarshall()
    {
        int[,] distance = (int[,])adjacencyMatrix.Clone();

        for (int i = 0; i < distance.GetLength(0); i++)
        for (int j = 0; j < distance.GetLength(0); j++)
            if (distance[i, j] == 0 && i != j)
                distance[i, j] = int.MaxValue;

        for (int k = 0; k < distance.GetLength(0); k++)
        for (int i = 0; i < distance.GetLength(0); i++)
        for (int j = 0; j < distance.GetLength(0); j++)
            if (distance[i, k] + distance[k, j] < distance[i, j] && distance[i, k] != int.MaxValue &&
                distance[k, j] != int.MaxValue)
                distance[i, j] = distance[i, k] + distance[k, j];

        return distance;
    }

    public Dictionary<int, List<int>> GetAdjacencyList()
    {
        Dictionary<int, List<int>> adjList = new();
        for (int i = 0; i < adjacencyMatrix.GetLength(0); i++)
        {
            List<int> adjacent = new();
            for (int j = 0; j < adjacencyMatrix.GetLength(1); j++)
                if (adjacencyMatrix[i, j] > 0)
                    adjacent.Add(j);
            adjList.Add(i, adjacent);
        }

        return adjList;
    }
}