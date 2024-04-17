using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace s5_tpo_lw_08;

public abstract class EdgeListBase: IGraphRepresentation, IEnumerable<KeyValuePair<(int from, int to), double>>
{
    public readonly int Size;
    protected readonly Dictionary<(int from, int to), double> _data;

    protected EdgeListBase(int size)
    {
        Size = size;
        _data = new Dictionary<(int from, int to), double>();
    }
    protected EdgeListBase(Dictionary<(int from, int to), double> data)
    {
        if (!_dataValidate(data)) 
            throw new ArgumentException("This dictionary is not a valid edge list.");
        Size = data.Select(edge => Math.Max(edge.Key.from, edge.Key.to)).DefaultIfEmpty(-1).Max() + 1;
        _data = data;
    }

    protected EdgeListBase(Dictionary<(int from, int to), double> data, int size)
    {
        if (!_dataValidate(data)) 
            throw new ArgumentException("This dictionary is not a valid edge list.");
        Size = size;
        foreach (KeyValuePair<(int from, int to),double> edge in data)
            Add(edge.Key, edge.Value);
    }

    public void Add((int from, int to) path, double distance)
    {
        _edgeValidate((path.from, path.to), distance);
        if (_data.ContainsKey(path) || _data.ContainsKey(path.Reverse()))
            throw new ArgumentException($"Path between {path.from} and {path.to} already exists.");
        _data.Add(path.from < path.to ? path : path.Reverse(), distance);
    }

    public void Remove((int from, int to) path)
    {
        _edgeValidate((path.from, path.to));
        if (!_data.ContainsKey(path) || _data.ContainsKey(path.Reverse()))
            throw new ArgumentException($"Path between {path.from} and {path.to} does not exists.");
        _data.Remove(path.from < path.to ? path : path.Reverse());
    }

    protected static bool _dataValidate(Dictionary<(int, int), double> data)
    {
        if (data.Count == 0) return false;
        List<(int, int)> uniques = new();
        foreach (KeyValuePair<(int from, int to), double> edge in data)
        {
            if (uniques.Contains(edge.Key) || uniques.Contains(edge.Key.Reverse())) 
                return false;
            uniques.Add(edge.Key);
            uniques.Add(edge.Key.Reverse());
        }
        return true;
    }

    protected void _edgeValidate((int from, int to) path, double distance = 1)
    {
        if (path.from == path.to) throw new ArgumentException("Nodes must be differ.");
        if (path.from < 0 || path.to < 0) throw new ArgumentException("Nodes must be greater than zero.");
        if (path.from > Size || path.to > Size) throw new ArgumentException("Nodes must be less than graph size.");
        if (distance <= 0) throw new ArgumentException("Distance must be positive.");
    }

    public IEnumerator<KeyValuePair<(int from, int to), double>> GetEnumerator() => _data.GetEnumerator();
    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    
    public override string ToString() => $"{{{string.Join(", ", _data)}}}";
}