namespace s5_tpo_lw_08;

public interface IGraphRepresentation { }

public interface IConvertibleTo<out TRepresentation>
where TRepresentation : IGraphRepresentation
{
    TRepresentation Convert();
}