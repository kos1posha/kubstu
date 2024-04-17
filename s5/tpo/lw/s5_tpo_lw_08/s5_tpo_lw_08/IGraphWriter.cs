namespace s5_tpo_lw_08;

public interface IGraphWriter<in TRepresentation>
where TRepresentation : IGraphRepresentation
{
    bool Write(string path, TRepresentation representation);
}