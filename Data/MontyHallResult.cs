namespace MontyHall.Data;

public record MontyHallResult
{
    public short wonChaging { get; set; }

    public short wonNotChanging { get; set; }

    public MontyHallResult(short _wonChaging, short _wonNotChanging)
    {
        wonChaging = _wonChaging;
        wonNotChanging = _wonNotChanging;
    }
}