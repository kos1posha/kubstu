using System.Collections.Generic;

namespace s5_tpo_lw_08;

public class DummyELReader: IGraphReader<EdgeList>
{
    public EdgeList Read(string path)
    {
        return new EdgeList(new Dictionary<(int from, int to), double>
        {
            { ( 0, 1 ), 40 },
            { ( 0, 4 ), 18 },
            { ( 1, 2 ), 22 },
            { ( 1, 3 ),  6 },
            { ( 1, 4 ), 15 },
            { ( 2, 3 ), 14 },
            { ( 3, 4 ), 20 }
        });
    }
}