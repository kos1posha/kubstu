namespace s5_tpo_lw_08;

public class DummyELWriter: IGraphWriter<EdgeList>
{
    public bool Write(string path, EdgeList representation) => true;
}