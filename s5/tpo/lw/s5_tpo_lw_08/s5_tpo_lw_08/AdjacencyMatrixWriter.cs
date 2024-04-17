namespace s5_tpo_lw_08;

public class DummyAMWriter: IGraphWriter<AdjacencyMatrixBase>
{
    public bool Write(string path, AdjacencyMatrixBase representation) => true;
}