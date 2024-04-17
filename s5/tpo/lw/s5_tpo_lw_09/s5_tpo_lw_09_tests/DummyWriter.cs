using System;
using System.Collections.Generic;
using System.IO;
using s5_tpo_lw_09;

namespace s5_tpo_lw_09_tests;

public class DummyWriter : IGraphWriter
{
    public void SaveAdjacencyList(TextWriter writer, List<List<int>> list)
    {
        throw new NotImplementedException();
    }
}