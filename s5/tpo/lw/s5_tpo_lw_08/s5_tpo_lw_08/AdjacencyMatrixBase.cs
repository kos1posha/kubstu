using System;

namespace s5_tpo_lw_08;

public abstract class AdjacencyMatrixBase : IGraphRepresentation
{
    public readonly int Size;
    private readonly double[,] _data;

    protected AdjacencyMatrixBase(int size)
    {
        Size = size;
        _data = new double[size, size];
    }
    protected AdjacencyMatrixBase(double[,] data)
    {
        if (!_dataValidate(data)) 
            throw new ArgumentException("This matrix is not an adjacency matrix.");
        Size = data.GetLength(0);
        _data = data;
    }
    
    public double this[int row, int column]
    {
        get => _data[row, column];
        set { _data[row, column] = value; _data[column, row] = value; }
    }
    
    protected static bool _dataValidate(double[,] data)
    {
        int size = data.GetLength(0);
        if (size < 2 || size !=  data.GetLength(1)) return false;
        for (int i = 0; i < size; i++)
        {
            if (data[i, i] != 0) return false;
            for (int j = 1; j < size - i; j++)
                if (!(double.IsInfinity(data[i, j]) && double.IsInfinity(data[i, j])))
                    if (Math.Abs(data[i, j] - data[j, i]) > 0.00001) 
                        return false;
        }
        return true;
    }

    public override string ToString()
    {
        string result = string.Empty;
        for (int i = 0; i < Size; i++, result+='\n')
            for (int j = 0; j < Size; j++)
                result += $"{this[i, j]}\t";
        return result.TrimEnd('\n');
    }
}