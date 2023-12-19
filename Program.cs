using MontyHall.Data;

namespace MontyHall;

public class Program
{
    public static int GenRandomDoor(Random random)
        => random.Next(1, 3);

    public static int RunExperiment(bool changeDoor, Random random)
    {
        var firstDoor = GenRandomDoor(random);
        var prizeDoor = GenRandomDoor(random);

        var possibleRevealedDoors = new List<int> { 1, 2, 3 }
            .Except(new List<int> { firstDoor, prizeDoor })
            .ToList();

        var revealedDoor = possibleRevealedDoors[random.Next(possibleRevealedDoors.Count)];

        if (changeDoor)
        {
            int secondDoor = 6 - revealedDoor - firstDoor;
            return secondDoor == prizeDoor ? 1 : 0;
        }
        else
        {
            return firstDoor == prizeDoor ? 1 : 0;
        }
    }

    public static void Main()
    {
        var random = new Random();
    }
}
