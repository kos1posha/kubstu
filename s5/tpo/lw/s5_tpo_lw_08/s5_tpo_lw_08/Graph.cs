using System;

namespace s5_tpo_lw_08;

public class Graph<TRepresentation, TReader, TWriter>
where TRepresentation : IGraphRepresentation, IConvertibleTo<TWriter>
where TReader : IGraphRepresentation, IConvertibleTo<TRepresentation>
where TWriter : IGraphRepresentation
{
    public readonly IGraphReader<TReader> Reader;
    public readonly IGraphWriter<TWriter> Writer;

    public TRepresentation Representation;

    public Graph(IGraphReader<TReader> graphReader, IGraphWriter<TWriter> graphWriter)
    {
        Reader = graphReader;
        Writer = graphWriter;
    }

    public void ReadFromFile(string path)
    {
        if (Representation is not null) throw new InvalidOperationException("This graph is already loaded.");
        IConvertibleTo<TRepresentation> readerRepresentation = Reader.Read(path);
        Representation = readerRepresentation.Convert();
    }
    
    public bool WriteToFile(string path) => Writer.Write(path, Representation.Convert());

    public override string ToString() => Representation.ToString();
}