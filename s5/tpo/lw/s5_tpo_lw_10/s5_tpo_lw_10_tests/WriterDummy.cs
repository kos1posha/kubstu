using System;
using System.Collections.Generic;
using s5_tpo_lw_10;

namespace s5_tpo_lw_10_tests;

public class WriterDummy : IGraphWriter
{
    public void SaveGraph(string path, Dictionary<int, List<int>> adj_list)
    {
        throw new NotImplementedException();
    }
}