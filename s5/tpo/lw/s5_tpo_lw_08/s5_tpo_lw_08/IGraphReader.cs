namespace s5_tpo_lw_08;

public interface IGraphReader<out TRepresentation>
where TRepresentation : IGraphRepresentation
{ 
    TRepresentation Read(string path);
}