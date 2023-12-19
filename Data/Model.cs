namespace MontyHall.Data;

public record Model
{
    public int wonChanging;
    public int wonNotChanging;

    public Model(int _wonChanging, int _wonNotChanging)
    {
        wonChanging = _wonChanging;
        wonNotChanging = _wonNotChanging;
    }
}